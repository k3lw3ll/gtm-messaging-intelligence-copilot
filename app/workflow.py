import os
from typing import Dict

from openai import OpenAI

from app.prompts import build_analysis_prompt
from app.schemas import empty_analysis_result


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def run_analysis(
    transcript_path: str,
    product_messaging_path: str,
    positioning_notes_path: str,
    competitor_notes_path: str = None,
    model: str = "gpt-4o-mini"
) -> Dict:
    """
    Runs the GTM messaging intelligence workflow.
    """

    transcript = load_file(transcript_path)
    product_messaging = load_file(product_messaging_path)
    positioning_notes = load_file(positioning_notes_path)

    competitor_notes = ""
    if competitor_notes_path and os.path.exists(competitor_notes_path):
        competitor_notes = load_file(competitor_notes_path)

    prompt = build_analysis_prompt(
        transcript=transcript,
        product_messaging=product_messaging,
        positioning_notes=positioning_notes,
        competitor_notes=competitor_notes
    )

    response = client.responses.create(
        model=model,
        input=prompt,
        temperature=0.3
    )

    raw_output = response.output_text

    # Attempt to parse JSON safely
    try:
        import json
        parsed = json.loads(raw_output)
    except Exception:
        parsed = empty_analysis_result()
        parsed["error"] = "Failed to parse model output"
        parsed["raw_output"] = raw_output

    return parsed


def save_output(data: Dict, output_path: str):
    import json
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)