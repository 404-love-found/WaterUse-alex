from together import Together
import os
import datetime

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# Input Files
odd_path = os.path.join(base_path, "Txts", "odd.txt")
game_path = os.path.join(base_path, "Txts", "game_stuff.txt")

# Output File (Saved in JUD_ALL folder)
output_path = os.path.join(base_path, "JUD_ALL", "all_models_comparison_updated.md")

# Top 3 Models (Consistent with unified_ab_test.py)
models_to_test = [
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "Qwen/Qwen2.5-72B-Instruct-Turbo"
]

def run_all_models():
    print("🚀 Starting Batch Generation for JUD_ALL...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError:
        print("❌ Error: Input files not found.")
        return

    # Standardized Prompt
    prompt = f"""
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

    print(f"🚀 Preparing output, results will be saved to: {output_path}\n")

    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(f"# 🏆 Unified Model Comparison (JUD_ALL Version)\n")
        out_file.write(f"> Generated at: {datetime.datetime.now()}\n\n")

        for model_name in models_to_test:
            print(f"⏳ Requesting model: {model_name} (this may take a while)...")
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.6
                )

                output_text = response.choices[0].message.content

                out_file.write(f"## 🤖 Model: `{model_name}`\n")
                out_file.write("---\n")
                out_file.write(output_text)
                out_file.write("\n\n<br><br><hr><br><br>\n\n")

                print(f"✅ {model_name} completed successfully!")

            except Exception as e:
                print(f"❌ Model {model_name} request failed: {e}")
                out_file.write(f"## 🤖 Model: `{model_name}`\n\n**Error**: {e}\n\n---\n\n")

    print(f"\n🎉 All completed! Please open `{output_path}` in VS Code or Markdown viewer.")

if __name__ == "__main__":
    run_all_models()