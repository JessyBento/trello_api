# main.py
import config.py
from report_generator.report_generator import generate_board_report

if __name__ == "__main__":
    # Substituir com suas credenciais e nome do quadro
    api_key = API_KEY
    token = TOKEN
    board_name = 'NomeDoQuadro'

    report_file = generate_board_report(api_key, token, board_name)
    print(f"Relatório gerado: {report_file}")
