"""
Run the 3 LLM models 30 times on the electricity ODD plus game_stuff text.

Models:
  - DeepSeek-R1
  - Llama-3.3-70B-Instruct-Turbo
  - Qwen2.5-7B-Instruct-Turbo
"""

import os
import time

from together import Together


api_key = os.getenv("TOGETHER_API_KEY", "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc")

MODELS = {
    "DeepSeek-R1": {
        "model_id": "deepseek-ai/DeepSeek-R1",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Llama-3.3-70B": {
        "model_id": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "timeout": 180.0,
        "max_tokens": 8192,
    },
    "Qwen2.5-7B": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "timeout": 180.0,
        "max_tokens": 8192,
    },
}

N_RUNS = 30
MAX_RETRIES = 5
BASE_WAIT = 30

current_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(current_dir, "Txts", "TXT")
odd_path = os.path.join(text_dir, "odd.txt")
game_path = os.path.join(text_dir, "game_stuff.txt")
output_dir = os.path.join(current_dir, "Batch_30Runs")


def build_prompt(odd_text, game_text):
    return f"""
    Given the following ODD+D description of an irrigation electricity governance model:
    {odd_text}

    Additional model logic and institutional details:
    {game_text}

    Extract all **distinct action situations** described in the model using the IAD framework.
    Each action situation must reflect a **unique strategic tension**.

    ### Task Requirements:
    1. Identify the distinct strategic dilemmas in the electricity governance model.
    2. For each dilemma, provide a **2-player Normal Form Payoff Matrix**.
    3. Reflect the relevant electricity-governance mechanisms, including farmer-farmer coordination,
       farmer-staff interaction, transformer capacity, capacitor adoption, authorization/enforcement,
       informal exchange, groundwater extraction, social learning, and bounded rationality.
    4. Do not invent action situations that are not grounded in the ODD+D text.
    5. Max fields = 10.

    Only output the analysis (Title, Tension, Matrix, Justification).
    """


def run_single(client, model_id, prompt, max_tokens):
    """Send one request with retry logic."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            error_msg = str(e).lower()
            retryable = any(k in error_msg for k in ["503", "service_unavailable", "timeout", "rate"])
            if retryable and attempt < MAX_RETRIES:
                wait = BASE_WAIT * attempt
                print(f"      ⚠️  Retry {attempt}/{MAX_RETRIES}, waiting {wait}s... ({e})")
                time.sleep(wait)
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

    with open(odd_path, "r", encoding="utf-8") as f:
        odd_text = f.read()
    with open(game_path, "r", encoding="utf-8") as f:
        game_text = f.read()

    prompt = build_prompt(odd_text, game_text)

    print(f"\n{'='*60}")
    print(f"  Model: {model_id}  |  {N_RUNS} runs")
    print(f"{'='*60}")

    for i in range(1, N_RUNS + 1):
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
            print("  ❌ failed")


if __name__ == "__main__":
    print(f"Output directory: {output_dir}")
    print(f"Input ODD: {odd_path}")
    print(f"Input Game Stuff: {game_path}")

    for model_key in MODELS:
        run_model_batch(model_key)

    print(f"\n{'='*60}")
    print(f"  All done! Results in: {output_dir}")
    print(f"{'='*60}")
