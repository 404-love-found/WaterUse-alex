from together import Together
import os
import time

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
# Set a long timeout (10 minutes) to allow DeepSeek-R1 to finish reasoning
client = Together(api_key=api_key, timeout=600.0)

model_name = "deepseek-ai/DeepSeek-R1"

# Dynamically get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to get the base path
base_path = os.path.dirname(current_dir)

# Input Files (Using Txts)
odd_path = os.path.join(base_path, "Txts", "odd.txt")
game_path = os.path.join(base_path, "Txts", "game_stuff.txt")

# Output File
output_file = os.path.join(current_dir, "DeepSeek_R1_Txts_Output.md")


def run_deepseek_r1_txts():
    print(f"🚀 Running Standalone Test for {model_name} (Txts version)...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError as e:
        print(f"❌ Error: Input files not found. \nDetails: {e}")
        return

    # Updated Standard Prompt based on Professor's instructions
    prompt = f"""
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
       - Reflect the **Spatial Asymmetry** (Upstream vs Downstream).
       - Reflect the **Ecological Thresholds** (Tipping points).
       - Max fields = 10.

    Only output the analysis (Title, Tension, Matrix, Justification).
    You may include your thought process, but ensure the final output is clearly structured.
    """

    print("   ↳ Sending request... (This may take several minutes for DeepSeek-R1)")

    # Auto-Retry Logic to handle server busy (503) or timeouts
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=8192
            )
            content = response.choices[0].message.content

            # Save Results
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# 🤖 Model Output: {model_name}\n")
                f.write(f"> Logic: Unified ODD+D Prompt (Txts)\n\n")
                f.write(content)

            print(f"✅ Output successfully saved to: {output_file}")
            break

        except Exception as e:
            error_msg = str(e).lower()
            if "503" in error_msg or "service_unavailable" in error_msg or "timeout" in error_msg:
                print(f"   ⚠️ Server busy or timeout. Retrying in 30 seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(30)
            else:
                print(f"❌ Unhandled Error: {e}")
                break
    else:
        print("❌ All retries failed. Please try again later.")


if __name__ == "__main__":
    run_deepseek_r1_txts()