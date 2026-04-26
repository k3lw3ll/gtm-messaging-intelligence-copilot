print("Starting analysis...")

from app.workflow import run_analysis, save_output


def main():
    result = run_analysis(
        transcript_path="data/transcripts/sample_call_01.txt",
        product_messaging_path="data/source_materials/product_messaging.md",
        positioning_notes_path="data/source_materials/positioning_notes.md",
        competitor_notes_path="data/source_materials/competitor_notes.md",
        model="gpt-4o-mini"
    )

    save_output(
        data=result,
        output_path="output/sample_call_01_analysis.json"
    )

    print("Analysis complete.")
    print("Output saved to output/sample_call_01_analysis.json")


if __name__ == "__main__":
    main()