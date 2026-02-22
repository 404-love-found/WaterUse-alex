from together import Together
import os

# 1. 直接填入你的 API Key（测试完务必记得去官网重置/删除该 Key）
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

# 2. 绝对路径配置（100%能找到文件）
odd_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/odd.txt"
game_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/game_stuff.txt"
# 汇总结果保存的路径（保存为 Markdown 文件方便阅读表格）
output_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/all_models_comparison.md"

# 3. 读取底层文本
print("📂 正在读取 ODD+D 文本文件...")
with open(odd_path, "r", encoding="utf-8") as f:
    odd = f.read()

with open(game_path, "r", encoding="utf-8") as f:
    game = f.read()

# 4. 定义统一的 Prompt
prompt = f"""
Given the following ODD+D description of a water use model:

{odd}

Extract all **distinct action situations** described in the model using the IAD framework. Each action situation should reflect a **unique strategic tension**.
To help inspire diverse and concrete strategic tensions, consider parallels to the following sustainability-related games, each with its own type of dilemma:

- **Cooperation, Coordination, and Conflict Game** - **Game of Trust** - **Public Goods Game** - **Common Pool Resource Game** - **Channel Irrigation Game** - **Watershed Game** - **Negotiations Game** - **Dam Maintenance Game** - **Surface Water Game** - **Irrigation Game** - **Fishery Game** ### Output Instructions
For each action situation, specify the following elements from IAD in detail:
1. **Title**
2. **Location**
3. **Players**
4. **Roles**
5. **Actions**
6. **Control Rules**
7. **Information**
8. **Outcomes**
9. **Payoffs**
10. **Strategic Tension**
11. **Temporal Structure**
12. **Relevant Rules**

If the situation is strategic, turn the situation into a two-player normal form game.
Include the game description, the players, the actions, and a payoff matrix with realistic values.

Ensure all game elements make logical sense:
    - The available actions for each player must be rational, context-appropriate, and economically or behaviorally realistic.
    - The payoffs should reflect the likely consequences of each combined action.
Avoid symmetric payoff duplication unless the game is truly symmetric.

After listing all action situations and their initial payoff matrices:
- **Analyze the strategic core** of each situation.
- Explicitly **compare** all strategic action situations. If two or more have similar roles, structures, or upstream/downstream differences (e.g. In a decentralized regime, an upstream farmer has access to water first, while a downstream farmer accesses fish first).
Then you **must revise or replace** one of them to ensure strategic diversity.

Aim for **at least 4 clearly distinct types** of strategic dilemmas.

After the games have been generated, double check that it strictly fits the {game} description.  
- Players are rational
- In decentralized water use games, consider spatial asymmetries (upstream vs downstream impacts).

**Constraints:**
- The maximum number of fields a farmer can irrigate is 10.
- Suggested strategy options should be chosen from realistic field allocations.

**Your Output Must Include:**
1. A brief explanation of why the resulting game **does** or **does not** comply with the ODD+D description.
2. If the game does **not** comply, revise it. Show only the **revised** version.
3. If the game is symmetrical, revise it. (DF’s High payoff should drop significantly when UF overuses water).
4. A clearly formatted payoff matrix with meaningful, asymmetric values.

Only output revised, ODD+D-compliant games. Use clear Markdown formatting.
"""

# 5. 定义要跑的三个模型
models_to_test = [
    "deepseek-ai/DeepSeek-R1",
    "deepseek-ai/DeepSeek-V3",
    "meta-llama/Llama-3.3-70B-Instruct-Turbo"
]

# 6. 开始循环请求并写入同一个文件
print(f"🚀 准备开始生成，结果将汇总保存至: {output_path}\n")

with open(output_path, "w", encoding="utf-8") as out_file:
    # 写入文件大标题
    out_file.write("# 🏆 ODD+D Action Situations - 三大模型横向对比报告\n\n")

    for model_name in models_to_test:
        print(f"⏳ 正在请求模型: {model_name} (这可能需要一两分钟)...")
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system",
                     "content": "You are an expert in institutional analysis, game theory, agent-based modeling, and IAD/ODD+D frameworks."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            output_text = response.choices[0].message.content

            # 将该模型的结果追加写入汇总文件
            out_file.write(f"## 🤖 模型: `{model_name}`\n")
            out_file.write("---\n\n")
            out_file.write(output_text)
            out_file.write("\n\n<br><br>\n\n")  # 用换行和空行隔开不同的模型结果

            print(f"✅ {model_name} 生成完毕并已写入文件！")

        except Exception as e:
            print(f"❌ 模型 {model_name} 请求失败: {e}")
            out_file.write(f"## 🤖 模型: `{model_name}`\n\n**生成失败**: {e}\n\n---\n\n")

print(
    f"\n🎉 全部完成！请用支持 Markdown 的编辑器（如 VS Code, Typora 或直接在 GitHub/Notion 中）打开 `{output_path}` 查看直观对比数据。")