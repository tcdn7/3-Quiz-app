import json
from question import Question
from json import JSONDecodeError

def validate_record(rec: dict) -> None:
    if not isinstance(rec, dict):
        raise ValueError("Record must be a JSON object (dict).")
    for key in ("text", "options", "answer"):
        if key not in rec:
            raise ValueError(f"Missing required field: {key}")

    text_value = rec["text"]
    if not isinstance(text_value, str) or not text_value.strip():
        raise ValueError("Field 'text' must be a non-empty string.")

    options = rec["options"]
    if not isinstance(options, list) or len(options) !=4:
        raise ValueError("Field 'options' must be a list of 4 items.")
    if not all(isinstance(opt, str) and opt.strip() for opt in options):
        raise ValueError("Each option must be a non-empty string.")

    answer = rec["answer"]
    if not isinstance(answer, str):
        raise ValueError("Field 'answer' must be a string.")
    if answer.strip().upper() not in {"A", "B", "C", "D"}:
        raise ValueError("Field 'answer' must be one of: A, B, C, D.")
    
    return None

def load_questions_from_json(path: str) -> list[Question]:
    """Load questions from a JSON file and return a list of Question objects."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"JSON file not found: {path}") from e
    except JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e

    if not isinstance(data, list):
        raise ValueError("Top-level JSON must be a list of records.")

    questions: list[Question] = []
    for idx, rec in enumerate(data, start=1):
        validate_record(rec)

        text_value = rec["text"].strip()
        opts = [o.strip() for o in rec["options"]]
        answer = rec["answer"].strip().upper()

        labelled = [
            f"A) {opts[0]}",
            f"B) {opts[1]}",
            f"C) {opts[2]}",
            f"D) {opts[3]}",
        ]

        questions.append(Question(text=text_value, options=labelled, answer=answer))

    if not questions:
        print("Warning: questions list is empty.")

    return questions