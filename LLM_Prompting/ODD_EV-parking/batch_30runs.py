"""
Run 30 ODD+game_stuff action-situation extraction trials for each model.

Models:
  - DeepSeek-R1
  - Llama-3.3-70B-Instruct-Turbo
  - Qwen2.5-7B-Instruct-Turbo

This mirrors the water-use standard experiment while using the EV parking case.
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
}

N_RUNS = 30
MAX_RETRIES = 5
RETRY_WAIT_SECONDS = 30
TEMPERATURE = 0.6

current_dir = os.path.dirname(os.path.abspath(__file__))
odd_path = os.path.join(current_dir, "Txts", "odd.txt")
game_path = os.path.join(current_dir, "Txts", "game_stuff.txt")
output_dir = os.path.join(current_dir, "Batch_30Runs")


def build_prompt(odd_text, game_text):
    return f"""
    Given the following ODD+D description of an apartment EV parking shared-charging model:
    {odd_text}

    Case scenario and model-logic context:
    {game_text}

    Extract all **distinct action situations** described in the model using the IAD framework.
    Each action situation must reflect a **unique strategic tension** among actors.

    ### Task Requirements:
    1. Identify the distinct strategic dilemmas in the shared EV charging case.
    2. For each, provide a **2-player Normal Form Payoff Matrix**.
    3. Focus on local shared-charger governance, queue fairness, charger occupation, user-management interaction, and capacity governance.
    4. Do not treat ordinary implementation details, generic ABM processes, billing arithmetic, or output metrics as action situations.
    5. Max fields = 10.

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
                temperature=TEMPERATURE,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            error_msg = str(e).lower()
            if any(k in error_msg for k in ["503", "service_unavailable", "timeout"]):
                print(
                    f"      Retry {attempt + 1}/{MAX_RETRIES}, "
                    f"waiting {RETRY_WAIT_SECONDS}s... ({e})"
                )
                time.sleep(RETRY_WAIT_SECONDS)
            else:
                print(f"      Error: {e}")
                return None
    print(f"      All {MAX_RETRIES} retries failed.")
    return None


def run_model_batch(model_key):
    cfg = MODELS[model_key]
    model_id = cfg["model_id"]
    client = Together(api_key=api_key, timeout=cfg["timeout"])

    model_output_dir = os.path.join(output_dir, model_key)
    os.makedirs(model_output_dir, exist_ok=True)

    with open(odd_path, "r", encoding="utf-8") as f:
        odd_text = f.read()
    with open(game_path, "r", encoding="utf-8") as f:
        game_text = f.read()

    prompt = build_prompt(odd_text, game_text)

    print(f"\n{'=' * 60}")
    print(f"  Model: {model_id}  |  {N_RUNS} runs")
    print(f"  Params: temperature={TEMPERATURE}, max_tokens={cfg['max_tokens']}, timeout={cfg['timeout']}")
    print(f"{'=' * 60}")

    for i in range(1, N_RUNS + 1):
        print(f"  Run {i:2d}/{N_RUNS} ...", end="", flush=True)
        content = run_single(client, model_id, prompt, cfg["max_tokens"])

        if content:
            filepath = os.path.join(model_output_dir, f"run_{i:02d}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Run {i} - {model_id}\n\n")
                f.write(content)
            print(f" saved ({len(content)} chars)")
        else:
            print(" failed")


if __name__ == "__main__":
    print(f"Output directory: {output_dir}")
    print(f"Input ODD: {odd_path}")
    print(f"Input Game: {game_path}")

    for model_key in MODELS:
        run_model_batch(model_key)

    print(f"\n{'=' * 60}")
    print(f"  All done. Results in: {output_dir}")
    print(f"{'=' * 60}")
