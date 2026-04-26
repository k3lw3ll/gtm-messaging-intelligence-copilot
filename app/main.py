import os

from app.workflow import run_analysis, save_output


TRANSCRIPTS_DIR = "data/transcripts"
OUTPUT_DIR = "output"

PRODUCT_MESSAGING = "data/source_materials/product_messaging.md"
POSITIONING_NOTES = "data/source_materials/positioning_notes.md"
COMPETITOR_NOTES = "data/source_materials/competitor_notes.md"


def main():
    print("Starting batch analysis...")

    for filename in os.listdir(TRANSCRIPTS_DIR):
        if not filename.endswith(".txt"):
            continue

        transcript_path = os.path.join(TRANSCRIPTS_DIR, filename)

        print(f"Processing: {filename}")

        result = run_analysis(
            transcript_path=transcript_path,
            product_messaging_path=PRODUCT_MESSAGING,
            positioning_notes_path=POSITIONING_NOTES,
            competitor_notes_path=COMPETITOR_NOTES,
        )

        output_filename = filename.replace(".txt", "_analysis.json")
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        save_output(result, output_path)

        print(f"Saved: {output_filename}")

    print("Batch analysis complete.")


if __name__ == "__main__":
    main()