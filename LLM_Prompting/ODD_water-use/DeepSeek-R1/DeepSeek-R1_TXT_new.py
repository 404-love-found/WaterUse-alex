from together import Together
import os
import time

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key, timeout=600.0)

model_name = "deepseek-ai/DeepSeek-R1"

current_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(current_dir)

odd_path = os.path.join(base_path, "TXT_new", "odd.txt")
game_path = os.path.join(base_path, "TXT_new", "GAME_STUFF_NEW.txt")

output_file = os.path.join(current_dir, "DeepSeek_R1_TXT_new_Output.md")


def run_deepseek_r1_txt_new():
    print(f"🚀 Running Standalone Test for {model_name} (TXT_new version)...")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd_text = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game_text = f.read()
    except FileNotFoundError as e:
        print(f"❌ Error: Input files not found. \nDetails: {e}")
        return

    # ⚠️ 为 DeepSeek-R1 优化的 Prompt (明确允许它展示思考过程)
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

    Please think step-by-step. You may output your thought process, but ensure your final response clearly presents the analysis (Title, Tension, Matrix, Justification).
    """

    print("   ↳ Sending request... (This may take several minutes for DeepSeek-R1)")

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=8192
            )

            # ⬇️ 核心诊断代码 (获取原始响应和结束原因)
            content = response.choices[0].message.content or ""
            finish_reason = response.choices[0].finish_reason

            print(f"\n   [DEBUG INFO]")
            print(f"   - Finish Reason: {finish_reason}")
            print(f"   - Content Length: {len(content)} characters")

            if len(content.strip()) == 0:
                print("   ⚠️ WARNING: The model returned an empty string! Checking raw response...")
                print(f"   Raw Response Dump: {response}")
            # ⬆️ 核心诊断代码结束

            # Save Results
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# 🤖 Model Output: {model_name}\n")
                f.write(f"> Logic: Unified ODD+D Prompt (TXT_new)\n")
                f.write(f"> Finish Reason: {finish_reason}\n\n")
                f.write(content)

            print(f"✅ Output successfully saved to: {output_file}")
            break

        except Exception as e:
            error_msg = str(e).lower()
            if "503" in error_msg or "service_unavailable" in error_msg or "timeout" in error_msg or "timed out" in error_msg:
                print(
                    f"   ⚠️ Server is busy or request timed out. Retrying in 30 seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(30)
            else:
                print(f"❌ Unhandled Error: {e}")
                break
    else:
        print("❌ All retries failed. The server is still too busy. Please try again later.")


if __name__ == "__main__":
    run_deepseek_r1_txt_new()