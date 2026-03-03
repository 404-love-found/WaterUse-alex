from together import Together
import os

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
# use same API Key
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

# the path
base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# Top 3 models
TARGET_MODELS = [
    "deepseek-ai/DeepSeek-R1",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    "Qwen/Qwen2.5-72B-Instruct-Turbo"
]


def check_available_models():
    print("🔍 Checking Together AI models...")
    try:
        models = client.models.list()

        available_ids = [m.id for m in models]

        print("\n✅ check targeted Top 3 models usage：")
        for target in TARGET_MODELS:
            status = "Usable" if target in available_ids else "not found"
            icon = "✅" if target in available_ids else "❌"
            print(f" {icon} {target}")

        return TARGET_MODELS
    except Exception as e:
        print(f"❌ Model fail: {e}")
        return []


def run_comparison_test(test_models):
    print("\n" + "=" * 50)
    print("🚀 TEST API...")


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
        print(f"❌ check path: {base_path}")
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
        print(f"\n⏳ CHECKING: {model_name} ...")
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=1000
            )

            output_text = response.choices[0].message.content
            safe_name = model_name.replace("/", "_")
            filename = os.path.join(output_dir, f"TEST_{safe_name}.txt")

            with open(filename, "w", encoding="utf-8") as out_file:
                out_file.write(f"Model: {model_name}\n")
                out_file.write("=" * 50 + "\n\n")
                out_file.write(output_text)

            print(f"✅ Success: {filename}")

        except Exception as e:
            print(f"❌ model {model_name} failure: {e}")


if __name__ == "__main__":
    check_available_models()
    run_comparison_test(TARGET_MODELS)