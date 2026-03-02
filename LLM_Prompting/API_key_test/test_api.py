import os
from together import Together

# 替换为你的 API Key
API_KEY = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=API_KEY)


def check_available_models():
    print("🔍 正在查询 Together AI 当前支持的顶级模型...")
    try:
        models = client.models.list()
        # 筛选出一些知名的 Instruct/Chat 模型
        keywords = ["llama-3", "deepseek", "qwen", "mistral"]
        available_models = [m.id for m in models if any(k in m.id.lower() for k in
                                                        keywords) and "instruct" in m.id.lower() or "v3" in m.id.lower() or "r1" in m.id.lower()]

        print("\n✅ 你的 API Key 可以使用的部分推荐模型如下：")
        for m in available_models:
            print(f" - {m}")
        return available_models
    except Exception as e:
        print(f"❌ 获取模型列表失败: {e}")
        return []


def run_comparison_test(test_models):
    print("\n" + "=" * 50)
    print("🚀 开始运行 ODD+D Action Situation 对比测试...")

    # 1. 获取绝对路径，确保能找到文件
    # 1. 直接使用硬编码的绝对路径（100%能找到）
    odd_path = "/LLM_Prompting/Txts/odd.txt"
    game_path = "/LLM_Prompting/Txts/game_stuff.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 如果上面的相对推导仍然找不到，你可以直接写死绝对路径，例如：
    # odd_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/odd.txt"
    # game_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/game_stuff.txt"
    output_dir = os.path.join(current_dir, "Model_Comparison_Results")

    try:
        with open(odd_path, "r", encoding="utf-8") as f:
            odd = f.read()
        with open(game_path, "r", encoding="utf-8") as f:
            game = f.read()
    except FileNotFoundError:
        print(f"❌ 找不到文本文件，请将以下路径替换为你在电脑上的绝对路径：\nodd: {odd_path}\ngame: {game_path}")
        return

    prompt = f"""
    Given the following ODD+D description of a water use model:
    {odd}

    Model details:
    {game}

    Extract 3 distinct action situations using the IAD framework.
    Requirements:
    1. Provide 3 distinct action situations representing different strategic dilemmas (e.g., Prisoner's Dilemma, Stag Hunt, Public Goods).
    2. Output a 2-player normal form payoff matrix for each.
    3. CONSTRAINTS: 
       - No completely symmetric matrices.
       - Matrices must reflect spatial asymmetries (upstream vs downstream).
       - Maximum irrigated fields is 10.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for model_name in test_models:
        print(f"\n⏳ 正在请求模型: {model_name} ...")
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are an expert in institutional analysis and game theory."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )

            output_text = response.choices[0].message.content
            safe_name = model_name.replace("/", "_")
            filename = os.path.join(output_dir, f"{safe_name}_output.txt")

            with open(filename, "w", encoding="utf-8") as out_file:
                out_file.write(f"Model: {model_name}\n")
                out_file.write("=" * 50 + "\n\n")
                out_file.write(output_text)

            print(f"✅ 成功！结果已保存至: {filename}")

        except Exception as e:
            print(f"❌ 模型 {model_name} 请求失败: {e}")


if __name__ == "__main__":
    # 1. 先看看有哪些模型可用
    available = check_available_models()

    # 2. 我们挑选 3 个目前公认最强、最适合逻辑推理的模型进行对比测试
    # 你可以根据上面打印出来的可用模型列表自行修改这三个名字
    target_models_to_test = [
        "deepseek-ai/DeepSeek-R1",
        "deepseek-ai/DeepSeek-V3",
        "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    ]

    print(f"\n🎯 准备测试以下选定模型: {target_models_to_test}")
    run_comparison_test(target_models_to_test)
    print("\n🎉 全部完成！请去 Model_Comparison_Results 文件夹查看结果。")