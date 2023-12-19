# main.py
from config.py import API_KEY, TOKEN, BOARD_NAME
from report_generator.report_generator import generate_board_report

if __name__ == "__main__":
    # Substituir com suas credenciais e nome do quadro
    api_key = API_KEY
    token = TOKEN
    board_name = BOARD_NAME

    report_file = generate_board_report(api_key, token, board_name)
    print(f"Relatório gerado: {report_file}")
