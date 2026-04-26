from typing import Any, Dict, List


ANALYSIS_SCHEMA: Dict[str, Any] = {
    "customer_themes": [
        {
            "theme": "",
            "evidence": "",
            "why_it_matters": ""
        }
    ],
    "objections": [
        {
            "objection": "",
            "evidence": "",
            "likely_source_of_confusion": ""
        }
    ],
    "customer_language": [
        {
            "phrase": "",
            "interpretation": ""
        }
    ],
    "messaging_gaps": [
        {
            "gap": "",
            "evidence": "",
            "recommendation": ""
        }
    ],
    "positioning_recommendations": [
        {
            "recommendation": "",
            "reasoning": "",
            "example_rewrite": ""
        }
    ],
    "field_enablement_notes": [
        {
            "note": "",
            "use_case": ""
        }
    ]
}


def empty_analysis_result() -> Dict[str, List[Dict[str, str]]]:
    """
    Returns a clean, structured output object for GTM messaging analysis.
    This is used as the target shape for LLM-generated output.
    """
    return {
        "customer_themes": [],
        "objections": [],
        "customer_language": [],
        "messaging_gaps": [],
        "positioning_recommendations": [],
        "field_enablement_notes": []
    }