# AI Writing Critique Tool

A command-line tool for generating structured, context-aware critique of writing.

This project treats AI as a **collaborative reasoning aid**, not an automated editor.  
Its purpose is to surface alignment, assumptions, and reasoning gaps while preserving
human authorship and intentional revision.

---

## What this tool does

Given a piece of writing, the tool produces **structured critique** across five dimensions:

1. **Thesis identification**  
   Identifies the central claim, or surfaces ambiguity if the thesis is unclear.

2. **Argument alignment**  
   Evaluates whether each major argument or section supports, weakens, or diverges from the thesis.

3. **Audience fit**  
   Assesses tone, assumptions, and framing relative to the intended audience.

4. **Grammar & syntax (bounded)**  
   Flags issues that materially affect clarity, without stylistic rewriting.

5. **Meta-feedback**  
   Explicitly lists assumptions made by the AI and what additional context would improve critique quality.

The tool does **not** rewrite text or generate polished prose.

---

## Why this exists

Much AI-based writing feedback fails because it:
- Critiques without understanding authorial intent
- Assumes an audience without making that assumption explicit
- Optimizes for polish rather than reasoning quality
- Replaces thinking instead of supporting it

This project is an attempt to design AI critique that is:
- **Context-aware**
- **Epistemically honest**
- **Non-authorial**
- **Iterative by design**

---

## How AI is used

AI is used to:
- Analyze structure and reasoning
- Surface misalignment between intent and execution
- Generate questions that support revision

AI is **not** used to:
- Rewrite essays
- Generate arguments on the author’s behalf
- Produce final or authoritative judgments

All outputs should be interpreted as **probabilistic critique**, not objective truth.

---

## Usage

```bash
python critique.py path/to/text.txt
