from together import Together
import os

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

model_name = "Qwen/Qwen2.5-7B-Instruct-Turbo"

# Dynamically get the directory of the current script (e.g., .../Qwen2.5-7B-Instruct-Turbo)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to get the base path (e.g., .../ODD_water-use)
base_path = os.path.dirname(current_dir)

# Input Files (Using Txts)
odd_path = os.path.join(base_path, "Txts", "odd.txt")
game_path = os.path.join(base_path, "Txts", "game_stuff.txt")

# Output File
output_file = os.path.join(current_dir, "Qwen2_5_7B_Txts_Output.md")

def run_qwen_2_5_7b_txts():
    print(f"🚀 Running Standalone Test for {model_name} (Txts version)...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError as e:
        print(f"❌ Error: Input files not found. \nDetails: {e}")
        # Print the exact paths being searched for easier debugging
        print(f"Looking for ODD at: {odd_path}")
        print(f"Looking for GAME at: {game_path}")
        return

    # Unified Standard Prompt
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
    """

    print("   ↳ Sending request...")
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )
        content = response.choices[0].message.content

        # Save Results
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# 🤖 Model Output: {model_name}\n")
            f.write(f"> Logic: Unified ODD+D Prompt (Txts)\n\n")
            f.write(content)

        print(f"✅ Output saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_qwen_2_5_7b_txts()