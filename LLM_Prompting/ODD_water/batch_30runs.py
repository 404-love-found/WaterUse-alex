"""
Run each configured LLM 30 times, with results saved under Batch_30Runs/.

All models use the same timeout, max-token limit, temperature, and prompt.
Qwen3.7-Plus uses streaming because that endpoint requires it.
"""

from together import Together
import os
import time

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
    raise RuntimeError("Set TOGETHER_API_KEY before running this script.")

MODELS = {
    "DeepSeek-R1": {
        "model_id": "deepseek-ai/DeepSeek-R1",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "DeepSeek-V4-Pro": {
        "model_id": "deepseek-ai/DeepSeek-V4-Pro",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Llama-3.3-70B": {
        "model_id": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Qwen2.5-7B": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Qwen3.7-Plus": {
        "model_id": "Qwen/Qwen3.7-Plus",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "gpt-oss-120b": {
        "model_id": "openai/gpt-oss-120b",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
}

N_RUNS = 30
MAX_RETRIES = 5
RETRY_WAIT_SECONDS = 30
RUN_START = int(os.environ.get("RUN_START", "1"))
RUN_END = int(os.environ.get("RUN_END", str(N_RUNS)))

# Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
odd_path = os.path.join(current_dir, "Txts", "odd.txt")
game_path = os.path.join(current_dir, "Txts", "game_stuff.txt")
output_dir = os.path.join(current_dir, "Batch_30Runs")


def build_prompt(odd_text, game_text):
    return f"""
    Given the following ODD+D description of a water use model:
    {odd_text}

    Model Logic & Math details:
    {game_text}

    Extract all **distinct action situations** described in the model using the IAD framework.
    Each action situation must reflect a **unique strategic tension**.

    ### Task Requirements:
    1. Identify the distinct strategic dilemmas.
    2. For each, provide a **2-player Normal Form Payoff Matrix**.
    3. **CRITICAL CONSTRAINTS**:
       - **Extract action situations ONLY for the decentralized case (DV). Do NOT extract situations for the centralized case (CV).**
       - Ignore centralized interactions such as National Authority forecasting/allocation; only farmer decisions under DV are in scope.
       - Reflect the **Spatial Asymmetry** (Upstream vs Downstream).
       - Reflect the **Ecological Thresholds** (Tipping points).
       - Max fields = 10.

    Only output the analysis (Title, Tension, Matrix, Justification).
    You may include your thought process, but ensure the final output is clearly structured.
    """


def run_single(client, model_id, prompt, max_tokens):
    """Send one request with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=max_tokens,
                stream=model_id == "Qwen/Qwen3.7-Plus",
            )
            if model_id == "Qwen/Qwen3.7-Plus":
                content_parts = []
                reasoning_parts = []
                for chunk in response:
                    if not getattr(chunk, "choices", None):
                        continue
                    delta = chunk.choices[0].delta
                    if getattr(delta, "content", None):
                        content_parts.append(delta.content)
                    if getattr(delta, "reasoning", None):
                        reasoning_parts.append(delta.reasoning)
                return "".join(content_parts) or "".join(reasoning_parts) or None

            message = response.choices[0].message
            return message.content or getattr(message, "reasoning", None)
        except Exception as e:
            error_msg = str(e).lower()
            if any(k in error_msg for k in ["503", "service_unavailable", "timeout", "rate", "429"]):
                print(
                    f"      ⚠️  Retry {attempt+1}/{MAX_RETRIES}, "
                    f"waiting {RETRY_WAIT_SECONDS}s... ({e})"
                )
                time.sleep(RETRY_WAIT_SECONDS)
            else:
                print(f"      ❌ Error: {e}")
                return None
    print(f"      ❌ All {MAX_RETRIES} retries failed.")
    return None


def run_model_batch(model_key):
    cfg = MODELS[model_key]
    model_id = cfg["model_id"]
    client = Together(api_key=api_key, timeout=cfg["timeout"])

    model_output_dir = os.path.join(output_dir, model_key)
    os.makedirs(model_output_dir, exist_ok=True)

    # Read input texts
    with open(odd_path, "r", encoding="utf-8") as f:
        odd_text = f.read()
    with open(game_path, "r", encoding="utf-8") as f:
        game_text = f.read()

    prompt = build_prompt(odd_text, game_text)

    print(f"\n{'='*60}")
    print(f"  Model: {model_id}  |  {N_RUNS} runs")
    print(f"{'='*60}")

    for i in range(RUN_START, RUN_END + 1):
        filepath = os.path.join(model_output_dir, f"run_{i:02d}.md")
        if os.path.exists(filepath):
            print(f"  Run {i:2d}/{N_RUNS} ... already exists, skipped")
            continue

        print(f"  Run {i:2d}/{N_RUNS} ...", end="", flush=True)
        content = run_single(client, model_id, prompt, cfg["max_tokens"])

        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Run {i} — {model_id}\n\n")
                f.write(content)
            print(f"  ✅ saved ({len(content)} chars)")
        else:
            print(f"  ❌ failed")


if __name__ == "__main__":
    print(f"Output directory: {output_dir}")
    print(f"Input ODD: {odd_path}")
    print(f"Input Game: {game_path}")

    requested_models = os.environ.get("MODEL_KEYS")
    selected_models = requested_models.split(",") if requested_models else list(MODELS)
    unknown_models = [model_key for model_key in selected_models if model_key not in MODELS]
    if unknown_models:
        raise ValueError(f"Unknown MODEL_KEYS: {', '.join(unknown_models)}")
    if not 1 <= RUN_START <= RUN_END <= N_RUNS:
        raise ValueError(f"Run range must satisfy 1 <= RUN_START <= RUN_END <= {N_RUNS}.")

    for model_key in selected_models:
        run_model_batch(model_key)

    print(f"\n{'='*60}")
    print(f"  All done! Results in: {output_dir}")
    print(f"{'='*60}")
