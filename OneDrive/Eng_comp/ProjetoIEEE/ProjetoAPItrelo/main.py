# main.py

from report_generator.report_generator import generate_board_report

if __name__ == "__main__":
    # Substituir com suas credenciais e nome do quadro
    api_key = 'sua-chave-de-api'
    token = 'seu-token-de-acesso'
    board_name = 'NomeDoQuadro'

    report_file = generate_board_report(api_key, token, board_name)
    print(f"Relatório gerado: {report_file}")
