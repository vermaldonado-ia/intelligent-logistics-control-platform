import json
from orchestrator import process_operation


def load_input_data(file_path: str) -> dict:
    """
    Carga los datos de entrada desde un archivo JSON.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    """
    Punto de entrada principal del MVP.
    """
    input_data = load_input_data("../data/sample_input.json")
    result = process_operation(input_data)

    print("\n=== RESULTADO FINAL DE LA OPERACIÓN ===")
    print(json.dumps(result, indent=4, ensure_ascii=False))

    if result["phone_notification"]["status"] == "generated":
        print("\nNotificación generada en: ../output/phone_notification.txt")

    if result["access_ticket"]["status"] == "generated":
        print("Ticket generado en: ../output/access_ticket.txt")


if __name__ == "__main__":
    main()