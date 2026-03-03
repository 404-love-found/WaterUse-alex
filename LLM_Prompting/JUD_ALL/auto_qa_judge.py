from together import Together
import os

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# Input: The output from run_all_and_save.py
input_md_path = os.path.join(base_path, "JUD_ALL", "all_models_comparison_updated.md")
output_report_path = os.path.join(base_path, "JUD_ALL", "QA_Verdict_Report.md")

# The Judge Model (Aligning with judge_with_mistakebook.py preference)
# Llama-3.3 is selected for its strict instruction following.
judge_model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"

def run_qa_judge():
    print(f"⚖️ Judge Agent [{judge_model}] is entering the court...")

    try:
        with open(input_md_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Report not found: {input_md_path}. Please run 'run_all_and_save.py' first.")
        return

    # Evaluation Prompt (Aligned with judge_with_mistakebook.py logic)
    judge_prompt = f"""
    You are a strict QA Judge evaluating an LLM's output for an Agent-Based Model design.

    Here is the full report containing outputs from multiple models:
    === REPORT START ===
    {content}
    === REPORT END ===

    Your Task:
    1. Analyze EACH model's output provided in the report.
    2. Rate specific Action Situations as [YES] (Pass) or [NO] (Fail).
    3. **Fail Criteria** (Strict Enforcement):
       - **Symmetric Payoffs**: e.g., 5,5 on diagonals for asymmetric roles (Upstream/Downstream).
       - **Hallucinations**: e.g., inventing pumps, tractors, or buying water (not in ODD+D).
       - **Lack of Diversity**: e.g., all scenarios are just "Prisoner's Dilemma".
       - **Ecological Ignorance**: Ignoring Tipping Points or fish collapse.

    Output Format (JSON-like structure):

    entry:
      model: [Model Name]
      verdict: [YES or NO]
      reason: [Concise explanation of failure or success]
      snippet: [Quote specific matrix or text causing the verdict]

    (Repeat for all distinct models found in the text)
    """

    print("   ↳ Judge is reviewing the document...")
    try:
        response = client.chat.completions.create(
            model=judge_model,
            messages=[{"role": "user", "content": judge_prompt}],
            temperature=0.1
        )

        judgement_text = response.choices[0].message.content

        # Save the full Verdict Report
        with open(output_report_path, "w", encoding="utf-8") as f:
            f.write("# ⚖️ Full Judge Verdict Report\n\n")
            f.write(f"> Judge Model: {judge_model}\n")
            f.write(f"> Evaluated File: {input_md_path}\n\n")
            f.write(judgement_text)

        print(f"✅ Verdict Complete! Full report saved to: {output_report_path}")
        print("👉 Check the report to see which models passed the 'Symmetry' and 'Constraint' tests.")

    except Exception as e:
        print(f"❌ Judge failed: {e}")

if __name__ == "__main__":
    run_qa_judge()