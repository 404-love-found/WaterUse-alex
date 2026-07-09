"""
Run the 3 LLM models 30 times on the Jennifer electricity ODD plus game_stuff text.

Models:
  - DeepSeek-R1
  - DeepSeek-V4-Pro
  - Llama-3.3-70B-Instruct-Turbo
  - Qwen2.5-7B-Instruct-Turbo
"""

import os
import time

from together import Together


api_key = os.environ.get("TOGETHER_API_KEY")
if not api_key:
    raise RuntimeError("Set TOGETHER_API_KEY before running this script.")

MODELS = {
    "DeepSeek-R1": {
        "model_id": "deepseek-ai/DeepSeek-R1",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "DeepSeek-V4-Pro": {
        "model_id": "deepseek-ai/DeepSeek-V4-Pro",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Llama-3.3-70B": {
        "model_id": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
    "Qwen2.5-7B": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "timeout": 600.0,
        "max_tokens": 16000,
    },
}

N_RUNS = 30
MAX_RETRIES = 5
BASE_WAIT = 30

current_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(current_dir, "Txts", "TXT")
odd_path = os.path.join(text_dir, "odd_jennifer.txt")
game_path = os.path.join(text_dir, "Electricity_game_stuff.txt")
output_dir = os.path.join(current_dir, "Batch_30Runs_Jennifer")

ODD_PROMPT_TEMPLATE = """
Given the following ODD+D description of an electricity-irrigation governance model:
 
{odd}
{game_block}
Extract all **distinct action situations** described in the model using the IAD framework. Each action situation should reflect a **distinct governance interaction** — this includes both strategic games (simultaneous decisions with interdependent payoffs) and non-strategic sequential processes (observation, experimentation, imitation). Do not merge separate interactions into one just because they share the same player types.
To help inspire diverse and concrete strategic tensions, consider parallels to the following sustainability-related games, each with its own type of dilemma:
 
- **Cooperation, Coordination, and Conflict Game** – In this set of games standard 2-player games on cooperation and coordination are framed in a natural resource management context. With this set of games we can see how small changes in the payoff matrix affect the nature of the social dilemma and expected outcomes.
- **Game of Trust** – With this game we can measure trust and trustworthiness. The trust game is played by two players, where the first player has to decide how much to trust player 2 by giving this player an amount of his/her resources. The amount given to player 2 will be increased and player 2 will demonstrate its trustworthiness by deciding how much to give back to player 1 and how much to keep for him/herself.
- **Public Goods Game** – This game is the classic public good game which captures a dilemma between what is good for the individual and for the group. An example is contributing to shared electricity infrastructure. If everyone contributes, everybody benefits, but if one person free-rides and does not contribute, that person will still get the benefits.
- **Common Pool Resource Game** – In this game participants share a common resource. We can create the situation of over-extraction, popularly known as the "tragedy of the commons". Applies to shared groundwater aquifers.
- **Authorization Game** – In this game players must decide whether to invest in formal authorization processes or bypass them. The outcome depends on the decisions of both the farmer seeking connection and the staff deciding whether to invest in service delivery.
- **Capacity Provision Game** – In this game players need to decide whether to contribute to shared electrical infrastructure capacity. They face a dilemma between individual cost-saving and collective reliability.
- **Collusion Exchange Game** – In this game players can mutually exchange favors or resources informally, creating a coordination problem between those who benefit from informal networks and those who do not.
- **DSM Coordination Game** – In this game farmers must decide whether to invest in demand-side management technologies. The benefit of adoption depends on how many neighbors also adopt, creating an assurance game.
- **Groundwater Extraction Game** – In this game participants share a groundwater aquifer and make extraction decisions. As the aquifer depletes, pumping energy costs rise, dynamically shifting the payoff structure over time.
- **Social Learning Game** – In this game farmers observe the outcomes of their neighbors' technology adoption decisions and update their own strategies accordingly. This is a non-strategic sequential process rather than a simultaneous game.
 
 
### Output Instructions
For each action situation, specify the following elements from IAD in detail:
 
1. **Title** – A concise name summarizing the action situation
2. **Location** – The physical or institutional setting where the action situation occurs (e.g., transformer group level, substation, regulatory office)
3. **Players** – The agents involved (e.g., farmers, substation staff), as defined by boundary rules
4. **Roles** – The roles players occupy (e.g., electricity consumer, enforcer, service provider, allocator)
5. **Actions** – The set of choices available to each player or role, per choice rules
6. **Control Rules** – How actions lead to outcomes, including any deterministic or stochastic effects
7. **Information** – What information players have access to (e.g., past voltage quality, peer adoption rates). Is it complete, partial, or noisy?
8. **Outcomes** – The results of actions (e.g., budget change, grid quality change, aquifer level change)
9. **Payoffs** – The consequences for each player, including economic, institutional, or ecological impacts
10. **Strategic Tension** – Does the situation involve any dilemmas between players? Clearly specify if the interaction is **strategic** or **non-strategic**. If the action situation is strategic, specify the type of game that would be used to model it.
    Prioritize the sustainability games mentioned. Include a short description of how/why there's this tension in this action situation.
11. **Temporal Structure** – Is the interaction one-shot, repeated annually, or continuous over time?
12. **Relevant Rules** – Describe any explicit boundary, position, choice, or control rules involved in the action situation
 
If the situation is strategic, turn the situation into a two-player normal form game.
Include the game description, the players, the actions, and a payoff matrix with realistic values.
 
Ensure all game elements make logical sense:
    - The available actions for each player must be rational, context-appropriate, and economically or behaviorally realistic.
    - The payoffs should reflect the likely consequences of each combined action (e.g., coordination failure, over-extraction, free-riding, informal exchange, authorization failure, etc.).
    - Do not include unrealistic or illogical actions unless justified.
Avoid symmetric payoff duplication unless the game is truly symmetric.
 
After listing all action situations and their initial payoff matrices:
 
- **Analyze the strategic core** of each situation (e.g., is it a coordination game, prisoner's dilemma, asymmetric conflict, etc.).
- Explicitly **compare** all strategic action situations. If two or more have similar:
  - Player roles or decision types
  - Payoff structures or incentive logic
  - Farmer and staff asymmetries
    In a decentralized regime, farmers negotiate directly with substation staff for connection and service. Staff have discretion over investment and authorization decisions.
    In a centralized regime, a utility authority allocates electricity access and mandates adoption decisions uniformly.
  - Social dilemmas (e.g., both are CPR or public goods)
 
Then you **must revise or replace** one of them to ensure strategic diversity.
 
Aim to extract **all governance interactions present in the model** — typically 5 to 6. Do not stop at 4 by merging distinct interactions. Strategic dilemmas and non-strategic sequential processes are both valid action situations and should both appear in the output.
Your goal is to produce a set of action situations where each one reflects a **different governance interaction**, not just different labels. Two interactions involving the same player types (e.g., farmer and staff) may still be distinct action situations if they involve different choices and different incentive structures.
 
For each game:
- Ensure that payoff values are grounded in the action situation: what does each agent gain or lose?
- There should be tension between the payoff values.
- Briefly explain why each outcome in the payoff matrix makes sense.
 
 
Some important points to consider:
    - Players are rational
    - In decentralized electricity-irrigation settings, consider institutional asymmetries:
        - Substation staff have discretionary power over connection authorization and service investment; farmers depend on this discretion.
        - Payoffs must reflect these power and information asymmetries even in simultaneous-move games.
    - Do not assume actions are made in isolation. Use the control rules and institutional logic from the model to define interaction effects.
    - Ensure payoffs reflect environmental feedback (e.g., aquifer depletion increasing pumping costs, voltage quality degradation from overload, budget constraints, collusion network density).
    - Avoid identical or symmetric payoff matrices unless the situation explicitly supports it.
Specify why or why not each game complies with the ODD+D description. If it does not, revise the game to make it compliant with the ODD+D protocol.
The revised game should be the only ones shown in the actual output.
 
Please use clear, structured formatting. Number each action situation. Do not repeat strategic tensions across situations.
 
Most important: For each strategic action situation, the payoff matrix should use the structured format defined in the schema.
 
All payoffs MUST be ordinal ranks using only integers 0, 1, 2, or 3.
These represent preference order only, not numeric utilities.
3 = most preferred outcome, 0 = least preferred outcome.
Do NOT treat payoff differences as proportional.
Each game must be 2×2 (two players, two strategies each).
 
Each game should represent a distinct strategic tension with ordinal payoffs (integers 0–3) grounded in the electricity-irrigation governance context.
"""


def build_prompt(odd_text, game_text):
    game_block = f"""
Additional model logic and institutional details:
{game_text}
 
"""
    return ODD_PROMPT_TEMPLATE.replace("{odd}", odd_text).replace("{game_block}", game_block)


def run_single(client, model_id, prompt, max_tokens):
    """Send one request with retry logic."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=max_tokens,
            )
            message = response.choices[0].message
            return message.content or getattr(message, "reasoning", None)
        except Exception as e:
            error_msg = str(e).lower()
            retryable = any(k in error_msg for k in ["503", "service_unavailable", "timeout", "rate"])
            if retryable and attempt < MAX_RETRIES:
                wait = BASE_WAIT * attempt
                print(f"      ⚠️  Retry {attempt}/{MAX_RETRIES}, waiting {wait}s... ({e})")
                time.sleep(wait)
            else:
                print(f"      ❌ Error: {e}")
                return None

    print(f"      ❌ All {MAX_RETRIES} retries failed.")
    return None


def run_model_batch(model_key):
    cfg = MODELS[model_key]
    model_id = cfg["model_id"]
    client = Together(api_key=api_key, timeout=cfg["timeout"])

    model_output_dir = os.path.join(output_dir, model_key)
    os.makedirs(model_output_dir, exist_ok=True)

    with open(odd_path, "r", encoding="utf-8") as f:
        odd_text = f.read()
    with open(game_path, "r", encoding="utf-8") as f:
        game_text = f.read()

    prompt = build_prompt(odd_text, game_text)

    print(f"\n{'='*60}")
    print(f"  Model: {model_id}  |  {N_RUNS} runs")
    print(f"{'='*60}")

    for i in range(1, N_RUNS + 1):
        filepath = os.path.join(model_output_dir, f"run_{i:02d}.md")
        if os.path.exists(filepath):
            print(f"  Run {i:2d}/{N_RUNS} ... already exists, skipped")
            continue

        print(f"  Run {i:2d}/{N_RUNS} ...", end="", flush=True)
        content = run_single(client, model_id, prompt, cfg["max_tokens"])

        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# Run {i} — {model_id}\n\n")
                f.write(content)
            print(f"  ✅ saved ({len(content)} chars)")
        else:
            print("  ❌ failed")


if __name__ == "__main__":
    print(f"Output directory: {output_dir}")
    print(f"Input ODD: {odd_path}")
    print(f"Input Game Stuff: {game_path}")

    for model_key in MODELS:
        run_model_batch(model_key)

    print(f"\n{'='*60}")
    print(f"  All done! Results in: {output_dir}")
    print(f"{'='*60}")
