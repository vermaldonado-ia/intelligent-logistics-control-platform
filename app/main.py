import json
from pathlib import Path

from app.orchestrator import process_operation


def load_sample_input() -> dict:
    """
    Carga un archivo sample_input.json desde la carpeta sample_data.
    """
    sample_path = Path("sample_data/sample_input.json")

    with sample_path.open("r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    input_data = load_sample_input()
    result = process_operation(input_data)

    print(json.dumps(result, indent=4, ensure_ascii=False))
