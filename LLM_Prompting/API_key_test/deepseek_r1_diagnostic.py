from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

from together import Together


CURRENT_DIR = Path(__file__).resolve().parent
OUTPUT = CURRENT_DIR / "deepseek_r1_diagnostic_report.txt"

DEEPSEEK_R1_EXACT = "deepseek-ai/DeepSeek-R1"
R1_RELATED_CANDIDATES = [
    "deepseek-ai/DeepSeek-R1",
    "deepseek-ai/DeepSeek-R1-0528",
    "deepseek-ai/deepseek-R1-trt-fp4",
    "deepseek/deepseek-r1-fp4-trtllm-gb200",
]


def load_api_key() -> str:
    api_key = os.environ.get("TOGETHER_API_KEY")
    if not api_key:
        raise RuntimeError("Set TOGETHER_API_KEY in the active virtual environment before running this script.")
    return api_key


def compact_error(exc: Exception) -> str:
    message = str(exc)
    try:
        body = getattr(exc, "body", None)
        if body:
            message = json.dumps(body, ensure_ascii=False)
    except Exception:
        pass
    return f"{type(exc).__name__}: {message}"


def object_value(obj, key: str):
    if isinstance(obj, dict):
        return obj.get(key)
    return getattr(obj, key, None)


def list_relevant_models(client: Together) -> list[str]:
    models = client.models.list()
    items = getattr(models, "data", models)
    names = []
    for item in items:
        model_id = object_value(item, "id") or object_value(item, "name") or object_value(item, "model")
        if model_id and ("deepseek" in model_id.lower() or "r1" in model_id.lower()):
            names.append(str(model_id))
    return sorted(set(names))


def list_relevant_endpoints(client: Together) -> list[dict]:
    endpoints = client.endpoints.list()
    items = getattr(endpoints, "data", endpoints)
    rows = []
    for item in items:
        name = object_value(item, "name")
        model = object_value(item, "model")
        display_name = object_value(item, "display_name")
        haystack = " ".join(str(v or "") for v in (name, model, display_name)).lower()
        if "deepseek" in haystack or "r1" in haystack:
            rows.append(
                {
                    "id": object_value(item, "id"),
                    "name": name,
                    "model": model,
                    "state": object_value(item, "state") or object_value(item, "status"),
                    "display_name": display_name,
                }
            )
    return rows


def probe_chat(client: Together, model_id: str, max_tokens: int) -> tuple[bool, str]:
    try:
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": "Return only the word OK."}],
            temperature=0.6,
            max_tokens=max_tokens,
        )
        content = response.choices[0].message.content
        return True, repr(content[:200])
    except Exception as exc:
        return False, compact_error(exc)


def main() -> None:
    api_key = load_api_key()
    client = Together(api_key=api_key, timeout=600.0)

    lines = []
    lines.append("DeepSeek-R1 Together API Diagnostic")
    lines.append("=" * 72)
    lines.append(f"Timestamp: {datetime.now().isoformat(timespec='seconds')}")
    lines.append("API key: loaded from TOGETHER_API_KEY environment variable (redacted)")
    lines.append("Water-use reference parameters: timeout=600.0, max_tokens=16000, temperature=0.6")
    lines.append("")

    lines.append("1) Exact DeepSeek-R1 test")
    ok, detail = probe_chat(client, DEEPSEEK_R1_EXACT, max_tokens=16000)
    lines.append(f"Model: {DEEPSEEK_R1_EXACT}")
    lines.append(f"Result: {'SUCCESS' if ok else 'FAILED'}")
    lines.append(f"Detail: {detail}")
    lines.append("")

    lines.append("2) DeepSeek/R1-related model ids visible from client.models.list()")
    try:
        model_names = list_relevant_models(client)
        for name in model_names:
            lines.append(f"- {name}")
        if not model_names:
            lines.append("- none")
    except Exception as exc:
        lines.append(f"Could not list models: {compact_error(exc)}")
    lines.append("")

    lines.append("3) DeepSeek/R1-related endpoints visible from client.endpoints.list()")
    try:
        endpoints = list_relevant_endpoints(client)
        for row in endpoints:
            lines.append(
                "- "
                + ", ".join(
                    f"{key}={value}"
                    for key, value in row.items()
                    if value not in (None, "")
                )
            )
        if not endpoints:
            lines.append("- none")
    except Exception as exc:
        lines.append(f"Could not list endpoints: {compact_error(exc)}")
    lines.append("")

    lines.append("4) R1-related candidate chat probes")
    for candidate in R1_RELATED_CANDIDATES:
        ok, detail = probe_chat(client, candidate, max_tokens=2)
        lines.append(f"- {candidate}: {'SUCCESS' if ok else 'FAILED'}")
        lines.append(f"  Detail: {detail}")
    lines.append("")

    lines.append("Conclusion")
    lines.append("- If exact deepseek-ai/DeepSeek-R1 fails with model_not_available, the current API key cannot access the original serverless DeepSeek-R1 model used by the water-use run.")
    lines.append("- If R1 FP4 endpoints return 500/503, those endpoints are visible but not currently healthy enough for this experiment.")
    lines.append("- Do not run Llama/Qwen 30-run comparisons until the DeepSeek-R1 access issue is resolved, because the requested benchmark requires DeepSeek-R1 first.")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote diagnostic report: {OUTPUT}")


if __name__ == "__main__":
    main()
