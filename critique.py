# critique.py

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

import argparse
from prompts import (
    SYSTEM_PROMPT,
    THESIS_PROMPT,
    ALIGNMENT_PROMPT,
    AUDIENCE_PROMPT,
    GRAMMAR_PROMPT,
    META_PROMPT,
)


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






def run_ai(prompt: str, text: str, context: dict, label: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"""
TEXT:
{text}

CONTEXT (may be incomplete):
- Intended thesis: {context.get("thesis")}
- Target audience: {context.get("audience")}
- Draft stage: {context.get("stage")}

TASK:
{prompt}
"""
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()



def main():
    parser = argparse.ArgumentParser(description="AI Writing Critique Tool")
    parser.add_argument("file", help="Path to text file to critique")

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned critique steps without making API calls",
    )

    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Require confirmation before making API calls",
    )

    args = parser.parse_args()



    text = load_text(args.file)
    context = get_user_context()

    assumed = {k: v is None for k, v in context.items()}

    if any(assumed.values()):
        print("\nNote: Some context was not provided and will be inferred by the AI.")

    print("\n--- CRITIQUE START ---\n")

    sections = [
        ("Thesis Identification", THESIS_PROMPT),
        ("Argument Alignment", ALIGNMENT_PROMPT),
        ("Audience Fit", AUDIENCE_PROMPT),
        ("Grammar & Syntax", GRAMMAR_PROMPT),
        ("Meta Feedback", META_PROMPT),
    ]

    if args.confirm:
        print("\nThis operation will make multiple OpenAI API calls.")
        print("Estimated cost: low (short text, low temperature).\n")

        confirm = input("Continue? [y/N]: ").strip().lower()
        if confirm != "y":
            print("Aborted.")
            return

    for label, prompt in sections:
        print(f"\n## {label}\n")

        if args.dry_run:
            print("[DRY RUN] No API call made.")
            print("Prompt type:", label)
            continue

        output = run_ai(prompt, text, context, label)
        print(output)



    print("\n--- CRITIQUE END ---\n")


if __name__ == "__main__":
    main()
