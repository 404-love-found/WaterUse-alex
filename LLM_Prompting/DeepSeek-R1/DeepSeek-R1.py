from together import Together
import os

# 直接填入你的 API Key
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)


odd_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/odd.txt"
game_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting/Txts/game_stuff.txt"

with open(odd_path, "r", encoding="utf-8") as f:
    odd = f.read()

with open(game_path, "r", encoding="utf-8") as f:
    game = f.read()

prompt = f"""
Given the following ODD+D description of a water use model:

{odd}

Extract all **distinct action situations** described in the model using the IAD framework. Each action situation should reflect a **unique strategic tension**.
To help inspire diverse and concrete strategic tensions, consider parallels to the following sustainability-related games, each with its own type of dilemma:

- **Cooperation, Coordination, and Conflict Game** – In this set of games standard 2-player games on cooperation and coordination are framed in a natural resource management context. With this set of games we can see how small changes in the payoff matrix affect the nature of the social dilemma and expected outcomes.
- **Game of Trust** – With this game we can measure trust and truthworthiness. The trust game is played by two players, where the first player have to decide how much to trust player 2 by giving this player an amount of his/her resources. The amount given to player 2 will be increased and player 2 will demonstrate it’s trustworthiness by deciding how much to give back to player 1 and how much to keep for him/herself.
- **Public Goods Game** – This game is the classic public good game which captures a dilemma between what is good for the individual and for the group. An example is contributing labor to a community project. If everyone contributes to the project, everybody benefits, but if one person freerides and does not contribute labor, that person will still get the benefits.
- **Common Pool Resource Game** – In this game participants share a common resource. We can create the situation of over-harvesting, popularly known as the “tragedy of the common”.
- **Channel Irrigation Game** In this game players need to take water use decision in the face of water scarcity. They can chose to grow water efficient or water consumptive crops while water is only sufficient for every player to grow the water efficient crop.
- **Watershed Game** – In this game participants experience asymmetries in a watershed where upstream players experience different problems and incentives compared to those downstream. The players make decisions on land use and whether they want to provide or accept payments to compensate the consequences of upstream players.
- **Negotiations Game** – In this game players will be in a large group but make each round a decision in a 2-player game where one player has control and propose a solution to a negotiation, and the other player can accept. Each round the player will play with somebody else, and we will see whether this distribution negotiation lead to a group level agreement.
- **Dam Maintenance Game** – In this game players need to jointly contribute to a water harvesting infrastructure from which all group members receive benefits. The game is based on a public good game.
- **Surface Water Game** – This game features typical water management challenges faced by local communities. It is based on a common pool resource games. Players can take decisions on contributing to a water harvesting structure which makes water available for the group and water appropriation decisions framed as the choice of crops with different water efficiencies.
- **Irrigation Game** – In this game participants have to make decisions to invest in the irrigation system maintenance and to extract water for irrigating their individual plots.
- **Fishery Game** – In this game participants have to decide where to fish and how much to fish.


### Output Instructions
For each action situation, specify the following elements from IAD in detail:

1. **Title** – A concise name summarizing the action situation  
2. **Location** – The physical or institutional setting where the action situation occurs (e.g., farm level, river basin, regulatory office)  
3. **Players** – The agents involved (e.g., farmers, regulators), as defined by boundary rules  
4. **Roles** – The roles players occupy (e.g., irrigator, enforcer, allocator, predictor)  
5. **Actions** – The set of choices available to each player or role, per choice rules  
6. **Control Rules** – How actions lead to outcomes, including any deterministic or stochastic effects  
7. **Information** – What information players have access to (e.g., past inflow data, peer behavior). Is it complete, partial, or noisy?  
8. **Outcomes** – The results of actions (e.g., crop yield, budget change, fish population)  
9. **Payoffs** – The consequences for each player, including economic, institutional, or ecological impacts  
10. **Strategic Tension** – Does the situation involve any dilemmas between players? Clearly specify if the interaction is **strategic** or **non-strategic**. If the action situation is strategic, specify the type of game that would be used to model it. 
    Prioritize the sustainability games mentioned. Include a short description of how/why there's this tension in this action situation.
11. **Temporal Structure** – Is the interaction one-shot, repeated annually, or continuous over time?  
12. **Relevant Rules** – Describe any explicit boundary, position, choice, or control rules involved in the action situation

If the situation is strategic, turn the situation into a two-player normal form game.
Include the game description, the players, the actions, and a payoff matrix with realistic values.

Ensure all game elements make logical sense:
    - The available actions for each player must be rational, context-appropriate, and economically or behaviorally realistic.
    - The payoffs should reflect the likely consequences of each combined action (e.g., coordination failure, overuse, free-riding, trust, punishment, etc.).
    - Do not include unrealistic or illogical actions unless justified.
Avoid symmetric payoff duplication unless the game is truly symmetric.

After listing all action situations and their initial payoff matrices:

- **Analyze the strategic core** of each situation (e.g., is it a coordination game, prisoner’s dilemma, asymmetric conflict, etc.).
- Explicitly **compare** all strategic action situations. If two or more have similar:
  - Player roles or decision types
  - Payoff structures or incentive logic
  - Upstream farmer and downstream farmer differences
    In a decentralized regime, an upstream farmer has access to water first, while a downstream farmer accesses fish first
    In a centralized regime, the national authority allocates the same amount of water to each farmer
  - Social dilemmas (e.g., both are CPR or public goods)

Then you **must revise or replace** one of them to ensure strategic diversity.

Aim for **at least 4 clearly distinct types** of strategic dilemmas (e.g., tragedy of the commons).
Your goal is to produce a set of action situations where each one reflects a **different game-theoretic logic**, not just different labels.

For each game:
- Ensure that payoff values are grounded in the action situation: what does each agent gain or lose?.
- There should be tension between the payoff values.
- Briefly explain why each outcome in the payoff matrix makes sense.

After the games have been generated, double check that it strictly fits the {game} description.  
Some important points to consider:
    - Players are rational
    - In decentralized water use games, consider spatial asymmetries:
        - If one farmer is upstream, their actions can impact downstream users, but not vice versa.
        - Payoffs must reflect these hydrological relationships even in simultaneous-move games.
    - Do not assume actions are made in isolation. Use the control rules and spatial logic from the model to define interaction effects.
    - Ensure payoffs reflect environmental feedback (e.g., water scarcity, fish population decline, budget constraints, yield effects).
Specify why or why not each game complies with the odd+d description. If it does not, revise the game to make it compliant with the odd+d protocol. 
The revised game should be the only ones shown in the actual output.

**Constraints:**
- The maximum number of fields a farmer can irrigate is 10.
- Suggested strategy options should be chosen from realistic field allocations (e.g., 3 vs 7 fields, 2 vs 8, etc.).

**Your Output Must Include:**
2. A brief explanation of why the resulting game **does** or **does not** comply with the ODD+D description  
3. If the game does **not** comply, revise it. Show only the **revised** version  
4. if the game is symmetrical, revise it. Remember that in decentralized systems, 
    - DF’s High payoff should drop significantly when UF overuses water.
    - 
4. A clearly formatted payoff matrix with meaningful, asymmetric values that capture resource tension

Only output revised, ODD+D-compliant games.

Please use clear, structured formatting. Number each action situation. Do not repeat strategic tensions across situations.
"""

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "system",
            "content": "You are an expert in institutional analysis, game theory, agent-based modeling, and IAD/ODD+D frameworks."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.7
)

print(response.choices[0].message.content)