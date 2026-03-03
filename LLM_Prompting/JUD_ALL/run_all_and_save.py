from together import Together
import os
import datetime

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# [UPDATED] Now points to the NEW (Experimental) texts for production run
odd_path = os.path.join(base_path, "TXT_new", "ODD_NEW.txt")
game_path = os.path.join(base_path, "TXT_new", "GAME_STUFF_NEW.txt")

# Output File
output_path = os.path.join(base_path, "JUD_ALL", "Production_Run_Report.md")

# Top 3 Models
models_to_test = [
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "Qwen/Qwen2.5-72B-Instruct-Turbo"
]

def run_production_generation():
    print("🚀 Starting Production Run (Using ODD_NEW Data)...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Input files not found in {os.path.dirname(odd_path)}")
        return

    # Standardized Prompt (Consistent with unified_ab_test.py)
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
        out_file.write(f"# 🏆 Production Model Run (New ODD Source)\n")
        out_file.write(f"> Generated at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out_file.write(f"> Source: `ODD_NEW.txt` & `GAME_STUFF_NEW.txt`\n\n")

        for model_name in models_to_test:
            print(f"⏳ Requesting model: {model_name}...")
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

    print(f"\n🎉 Production run complete! File: {output_path}")

if __name__ == "__main__":
    run_production_generation()