from together import Together
import os
import datetime

# ---------------------------------------------------------
# 1. Configuration Area
# ---------------------------------------------------------
# Insert your API Key
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

# Base Directory Path (Ensure 'WaterUse——alex' matches your actual folder name)
base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# Path for the Unified Output Report
output_file = os.path.join(base_path, "Unified_Comparison_Report.md")

# Define Input Files for Control Group (OLD) and Experimental Group (NEW)
files_config = {
    "OLD": {
        "odd": os.path.join(base_path, "Txts", "odd.txt"),
        "game": os.path.join(base_path, "Txts", "game_stuff.txt")
    },
    "NEW": {
        "odd": os.path.join(base_path, "TXT_new", "ODD_NEW.txt"),
        "game": os.path.join(base_path, "TXT_new", "GAME_STUFF_NEW.txt")
    }
}

# [UPDATED] List of Top-Tier Models to Benchmark
# We use the 3 best models as requested to ensure maximum diversity and logic.
models = [
    "deepseek-ai/DeepSeek-R1",  # Best for Reasoning (Chain of Thought)
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Best for Instruction Following
    "Qwen/Qwen2.5-7B-Instruct-Turbo"  # Best Generalist / Logic Alternative
]


# ---------------------------------------------------------
# 2. Core Functions
# ---------------------------------------------------------
def get_prompt(odd_path, game_path):
    """
    Reads the text files and constructs the standardized prompt.
    """
    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError:
        return None

    return f"""
    Given the following ODD+D description of a water use model:
    {odd_text}

    Model Logic & Math details:
    {game_text}

    Extract all **distinct action situations** described in the model using the IAD framework. 
    Each action situation must reflect a **unique strategic tension**.

    ### Task Requirements:
    1. Identify at least 3-4 distinct strategic dilemmas.
    2. For each, provide a **2-player Normal Form Payoff Matrix**.
    3. **CRITICAL CONSTRAINT**: 
       - Reflect the **Spatial Asymmetry** (Upstream vs Downstream).
       - Reflect the **Ecological Thresholds** (Tipping points).
       - Max fields = 10.

    Only output the analysis (Title, Tension, Matrix, Justification).
    """


def run_test():
    print("🚀 Starting [Unified A/B Comparison Test] with Top 3 Models...")

    # Prepare Prompts for both versions
    prompt_old = get_prompt(files_config["OLD"]["odd"], files_config["OLD"]["game"])
    prompt_new = get_prompt(files_config["NEW"]["odd"], files_config["NEW"]["game"])

    if not prompt_old or not prompt_new:
        print("❌ Error: Input files not found. Please check file paths.")
        return

    # Open the report file for writing (Overwrites existing file)
    with open(output_file, "w", encoding="utf-8") as f:
        # Write Report Header
        f.write(f"# ⚔️ Unified A/B Comparison Report\n")
        f.write(f"> Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(
            "This report directly compares the **Old Source** vs. **New Source** outputs for each of the top 3 models.\n\n")

        for model in models:
            print(f"\n🤖 Benchmarking Model: {model}")
            f.write(f"# 🤖 Model: `{model}`\n")
            f.write("---\n")

            # --- 1. Run Old Version ---
            print("   ↳ Generating [OLD Version] Output...")
            try:
                resp_old = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt_old}],
                    temperature=0.6
                )
                content_old = resp_old.choices[0].message.content
            except Exception as e:
                content_old = f"Error: {e}"

            # Write Old Version Result
            f.write(f"## 🔴 [OLD Version] Output\n")
            f.write(f"> Source: Original odd.txt & game_stuff.txt\n\n")
            f.write(content_old)
            f.write("\n\n")

            # --- 2. Run New Version ---
            print("   ↳ Generating [NEW Version] Output...")
            try:
                resp_new = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt_new}],
                    temperature=0.6
                )
                content_new = resp_new.choices[0].message.content
            except Exception as e:
                content_new = f"Error: {e}"

            # Write New Version Result
            f.write(f"## 🟢 [NEW Version] Output\n")
            f.write(f"> Source: Revised ODD_NEW.txt & GAME_STUFF_NEW.txt\n\n")
            f.write(content_new)
            f.write("\n\n")

            # Visual Separator
            f.write("<br><br><hr><br><br>\n\n")
            print(f"   ✅ Model {model} completed!")

    print(f"\n🎉 Comparison complete! Report saved to: {output_file}")
    print("👉 Please open this file in VS Code and verify the improvements.")


if __name__ == "__main__":
    run_test()
