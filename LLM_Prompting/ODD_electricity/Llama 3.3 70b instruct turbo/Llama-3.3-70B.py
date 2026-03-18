from together import Together
import os

api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "LLM_Prompting/ODD_electricity"
model_name = "meta-llama/Llama-3.3-70B-Instruct-Turbo"

odd_path = os.path.join(base_path, "TXT_electricity", "ODD_electricity.txt")
scenario_path = os.path.join(base_path, "TXT_electricity", "SCENARIO_electricity.txt")
game_path = os.path.join(base_path, "TXT_electricity", "GAME_STUFF_electricity.txt")

output_dir = os.path.join(base_path, "Llama-3.3-70B")
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "Llama_3.3_70B_Standalone_Output.md")


def run_llama():
    print(f"🚀 Running Standalone Test for {model_name} (Electricity)...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(scenario_path, "r", encoding="utf-8") as f:
            scenario_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return

    prompt = f"""
    Given the following ODD+D description of an electricity governance model:
    {odd_text}

    Model Scenarios details:
    {scenario_text}

    Model Logic & Math details:
    {game_text}

    Extract all **distinct action situations** described in the model using the IAD framework. 
    Each action situation must reflect a **unique strategic tension**.

    ### Task Requirements:
    1. Identify all 6 distinct strategic dilemmas/links.
    2. For each valid strategic game, provide a **2-player Normal Form Payoff Matrix** using Ordinal Ranks (0, 1, 2, 3).
    3. **CRITICAL CONSTRAINT**: 
       - Distinguish clearly between simultaneous games (e.g., Stag Hunt, Asymmetric PD) and non-strategic sequential links.
       - Reflect the precise Network Linkages (τ, ι, δ, γ) that connect the situations.

    Only output the analysis (Title, Tension, Matrix, Justification).
    """

    print("   ↳ Sending request...")
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system",
                 "content": "You are an expert in game theory, institutional analysis, and social-ecological systems modeling."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4  #
        )
        content = response.choices[0].message.content

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Model Output: {model_name}\n\n")
            f.write(content)
        print(f"✅ Output saved to: {output_file}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    run_llama()