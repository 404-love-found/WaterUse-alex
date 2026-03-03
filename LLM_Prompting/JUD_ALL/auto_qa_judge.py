from together import Together
import os
import datetime

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
api_key = "tgp_v1_5DGhZ0hxAwmGKuR0WD_TfmoV0FTgWlHoym6h2G3FWJc"
client = Together(api_key=api_key)

base_path = "/Users/alex-lirio-lucian/WaterUse——alex/LLM_Prompting"

# Input: The output from the Production Run
input_md_path = os.path.join(base_path, "JUD_ALL", "Production_Run_Report.md")
output_report_path = os.path.join(base_path, "JUD_ALL", "QA_Verdict_Report.md")

# [UPDATED] Centralized Mistake Book (Same file as the root script uses)
mistake_book = os.path.join(base_path, "Mistake_Book.md")

# Judge Model
judge_model = "meta-llama/Llama-3.3-70B-Instruct-Turbo"


# ---------------------------------------------------------
# Mistake Logging Logic (Synced with judge_with_mistakebook.py)
# ---------------------------------------------------------
def log_mistake(model_name, version, reason, snippet):
    """
    Appends a failed test case to the central Mistake Book.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(mistake_book):
        with open(mistake_book, "w", encoding="utf-8") as f:
            f.write("# 📕 Agent Mistake Book (Failure Log)\n")
            f.write("> Records all cases rejected ([NO]) by the AI Judge.\n\n")

    with open(mistake_book, "a", encoding="utf-8") as f:
        f.write(f"## ❌ Mistake Record [{timestamp}] (from JUD_ALL)\n")
        f.write(f"- **Model**: `{model_name}`\n")
        f.write(f"- **Source Version**: {version}\n")
        f.write(f"- **Rejection Reason**: {reason}\n")
        f.write(f"- **Context Snippet**:\n> {snippet[:200]}...\n\n")
        f.write("---\n\n")


def run_qa_judge():
    print(f"⚖️ Judge Agent [{judge_model}] is reviewing Production Report...")

    try:
        with open(input_md_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Report not found: {input_md_path}. Run 'run_all_and_save.py' first.")
        return

    judge_prompt = f"""
    You are a strict QA Judge evaluating an LLM's output for an Agent-Based Model design.

    Here is the full report:
    === REPORT START ===
    {content}
    === REPORT END ===

    Your Task:
    1. Analyze EACH model's output.
    2. Rate Action Situations as [YES] (Pass) or [NO] (Fail).
    3. **Fail Criteria**:
       - **Symmetric Payoffs**: e.g., 5,5 on diagonals for asymmetric roles.
       - **Hallucinations**: e.g., pumps, tractors, buying water.
       - **Lack of Diversity**: e.g., only Prisoner's Dilemma.
       - **Ecological Ignorance**: No Tipping Points/Fish collapse.

    Output Format (JSON-like structure):

    entry:
      model: [Model Name]
      version: [Production]
      verdict: [YES or NO]
      reason: [Concise explanation]
      snippet: [First 20 words of bad text]
    """

    print("   ↳ Judge is analyzing...")
    try:
        response = client.chat.completions.create(
            model=judge_model,
            messages=[{"role": "user", "content": judge_prompt}],
            temperature=0.1
        )

        judgement_text = response.choices[0].message.content

        # Save Report
        with open(output_report_path, "w", encoding="utf-8") as f:
            f.write("# ⚖️ Production QA Verdict\n\n")
            f.write(judgement_text)

        print(f"✅ Verdict Saved: {output_report_path}")

        # --- Mistake Parser ---
        print("📝 Parsing and archiving mistakes...")
        lines = judgement_text.split('\n')
        current_model = "Unknown"
        current_version = "Production"
        count = 0

        for i, line in enumerate(lines):
            line = line.strip()
            if "model:" in line.lower():
                current_model = line.split(":", 1)[1].strip()

            if "verdict:" in line.lower() and "[no]" in line.lower():
                reason = "N/A"
                snippet = "N/A"
                # Look ahead for reason/snippet
                for j in range(i + 1, min(i + 5, len(lines))):
                    if "reason:" in lines[j].lower():
                        reason = lines[j].split(":", 1)[1].strip()
                    if "snippet:" in lines[j].lower():
                        snippet = lines[j].split(":", 1)[1].strip()

                log_mistake(current_model, current_version, reason, snippet)
                count += 1

        if count > 0:
            print(f"📕 Archived {count} failures to 'Mistake_Book.md'.")
        else:
            print("🎉 No failures found (or parsing mismatch).")

    except Exception as e:
        print(f"❌ Judge failed: {e}")


if __name__ == "__main__":
    run_qa_judge()