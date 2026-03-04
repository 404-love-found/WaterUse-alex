from together import Together
import os

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# A broad list of candidates including fallbacks for Qwen
CANDIDATE_MODELS = [
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "Qwen/Qwen2.5-72B-Instruct",  # Target
    "Qwen/Qwen2.5-7B-Instruct-Turbo",  # Fallback 1
    "Qwen/Qwen2-72B-Instruct",  # Fallback 2
    "Qwen/QwQ-32B-Preview",  # Fallback 3
    "mistralai/Mixtral-8x22B-Instruct-v0.1"  # Ultimate Fallback
]


def find_working_models():
    """
    Sends a tiny request to verify if the model is actually available
    on the public serverless endpoints, avoiding the 400 error.
    """
    working_models = []
    print("🔍 Probing Together AI to find active serverless models...\n")

    for model in CANDIDATE_MODELS:
        try:
            # Send a 1-token dummy request to test availability
            client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Hi"}],
                max_tokens=2
            )
            print(f"✅ [ACTIVE]: {model}")
            working_models.append(model)
        except Exception as e:
            # Catch the 400 error or any other unavailability errors silently
            print(f"❌ [UNAVAILABLE]: {model} (Moved to dedicated or offline)")

    print("\n==================================================")
    print(f"🎯 Total active models found: {len(working_models)}")
    return working_models


def run_comparison_test(test_models):
    if not test_models:
        print("❌ No valid models found to run the test.")
        return

    print("\n🚀 Starting Heavy Generation Test on ACTIVE models...")

    odd_path = os.path.join(base_path, "Txts", "odd.txt")
    game_path = os.path.join(base_path, "Txts", "game_stuff.txt")
    output_dir = os.path.join(base_path, "API_key_test", "Test_Output")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError:
        print(f"❌ Input files not found. Check path: {base_path}")
        return

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

    for model_name in test_models:
        print(f"\n⏳ GENERATING: {model_name} ...")
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=1500
            )

            output_text = response.choices[0].message.content
            safe_name = model_name.replace("/", "_")
            filename = os.path.join(output_dir, f"TEST_{safe_name}.txt")

            with open(filename, "w", encoding="utf-8") as out_file:
                out_file.write(f"Model: {model_name}\n")
                out_file.write("=" * 50 + "\n\n")
                out_file.write(output_text)

            print(f"✅ Success: Saved to {filename}")

        except Exception as e:
            print(f"❌ Model {model_name} failed during long generation: {e}")


if __name__ == "__main__":
    # 1. Filter out the dead models
    active_models = find_working_models()

    # 2. Pick top 3 active models to avoid taking too much time
    selected_top_3 = active_models[:3]
    print(f"👉 Proceeding with top 3 models: {selected_top_3}")

    # 3. Run the actual prompt
    run_comparison_test(selected_top_3)