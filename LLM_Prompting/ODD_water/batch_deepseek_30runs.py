

from together import Together
import os
import time

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
    raise RuntimeError("Set TOGETHER_API_KEY before running this script.")
model_id = "deepseek-ai/DeepSeek-R1"

N_RUNS = 30
MAX_RETRIES = 5
MAX_TOKENS = 16000
RETRY_WAIT_SECONDS = 30
COOLDOWN = 1    # seconds between successful runs (professor's suggestion)

current_dir = os.path.dirname(os.path.abspath(__file__))
odd_path = os.path.join(current_dir, "Txts", "odd.txt")
game_path = os.path.join(current_dir, "Txts", "game_stuff.txt")
output_dir = os.path.join(current_dir, "Batch_30Runs", "DeepSeek-R1")
error_log_path = os.path.join(output_dir, "error_log.txt")


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


def log_error(msg):
    with open(error_log_path, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def run_single(client, prompt, run_num):
    """Send one request with retry logic."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            t0 = time.time()
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=MAX_TOKENS,
            )
            dt = time.time() - t0
            content = response.choices[0].message.content
            finish = response.choices[0].finish_reason
            usage = response.usage

            if content and len(content.strip()) > 50:
                print(f"    [{dt:.0f}s, {usage.completion_tokens} tokens, finish={finish}]", end="")
                return content
            else:
                msg = (f"  Run {run_num} attempt {attempt}: empty response "
                       f"({len(content) if content else 0} chars, "
                       f"{usage.completion_tokens} completion_tokens, "
                       f"finish={finish}, {dt:.0f}s)")
                print(f"\n{msg}")
                log_error(msg)

        except Exception as e:
            msg = f"  Run {run_num} attempt {attempt}/{MAX_RETRIES}: {type(e).__name__}: {e}"
            print(f"\n{msg}")
            log_error(msg)
            if attempt < MAX_RETRIES:
                print(f"      Waiting {RETRY_WAIT_SECONDS}s before retry...")
                time.sleep(RETRY_WAIT_SECONDS)

        # Delay between retries
        time.sleep(COOLDOWN)
    return None


def main():
    os.makedirs(output_dir, exist_ok=True)

    with open(odd_path, "r", encoding="utf-8") as f:
        odd_text = f.read()
    with open(game_path, "r", encoding="utf-8") as f:
        game_text = f.read()

    prompt = build_prompt(odd_text, game_text)
    client = Together(api_key=api_key, timeout=600.0)

    # Clear error log
    with open(error_log_path, "w", encoding="utf-8") as f:
        f.write(f"DeepSeek-R1 Batch Run Error Log\n")
        f.write(f"max_tokens={MAX_TOKENS}, cooldown={COOLDOWN}s\n")
        f.write(f"{'='*50}\n\n")

    print(f"{'='*60}")
    print(f"  DeepSeek-R1  |  {N_RUNS} runs  |  max_tokens={MAX_TOKENS}")
    print(f"  Cooldown: {COOLDOWN}s between calls")
    print(f"{'='*60}")

    success = 0
    fail = 0

    for i in range(1, N_RUNS + 1):
        print(f"  Run {i:2d}/{N_RUNS} ...", end="", flush=True)
        content = run_single(client, prompt, i)

        if content:
            filepath = os.path.join(output_dir, f"run_{i:02d}.md")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Run {i} — {model_id}\n\n")
                f.write(content)
            print(f"  ✅ saved ({len(content)} chars)")
            success += 1
        else:
            log_error(f"Run {i}: ALL RETRIES FAILED\n")
            print(f"  ❌ all retries failed")
            fail += 1

        # Cooldown between runs
        if i < N_RUNS:
            time.sleep(COOLDOWN)

    print(f"\n{'='*60}")
    print(f"  Done!  Success: {success}/{N_RUNS}  |  Failed: {fail}/{N_RUNS}")
    print(f"  Results: {output_dir}")
    print(f"  Error log: {error_log_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
