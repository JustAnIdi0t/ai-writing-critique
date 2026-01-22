# critique.py

import argparse
from prompts import (
    SYSTEM_PROMPT,
    THESIS_PROMPT,
    ALIGNMENT_PROMPT,
    AUDIENCE_PROMPT,
    GRAMMAR_PROMPT,
    META_PROMPT,
)
from config import USE_MOCK_AI


def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def get_user_context():
    print("\n(Optional) Context — press Enter to skip.\n")

    thesis = input("Intended thesis: ").strip()
    audience = input("Target audience: ").strip()
    stage = input("Draft stage (exploratory / argumentative / near-final): ").strip()

    return {
        "thesis": thesis or None,
        "audience": audience or None,
        "stage": stage or None,
    }


def mock_ai_response(label: str) -> str:
    return f"[MOCK AI OUTPUT for {label}]"


def run_ai(prompt: str, text: str, context: dict, label: str) -> str:
    if USE_MOCK_AI:
        return mock_ai_response(label)

    # Later: replace with real AI call
    raise NotImplementedError("Real AI integration not implemented yet.")


def main():
    parser = argparse.ArgumentParser(description="AI Writing Critique Tool")
    parser.add_argument("file", help="Path to text file to critique")
    args = parser.parse_args()

    text = load_text(args.file)
    context = get_user_context()

    print("\n--- CRITIQUE START ---\n")

    sections = [
        ("Thesis Identification", THESIS_PROMPT),
        ("Argument Alignment", ALIGNMENT_PROMPT),
        ("Audience Fit", AUDIENCE_PROMPT),
        ("Grammar & Syntax", GRAMMAR_PROMPT),
        ("Meta Feedback", META_PROMPT),
    ]

    for label, prompt in sections:
        print(f"\n## {label}\n")
        output = run_ai(prompt, text, context, label)
        print(output)

    print("\n--- CRITIQUE END ---\n")


if __name__ == "__main__":
    main()
