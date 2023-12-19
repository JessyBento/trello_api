#COD PARA PEGAR NOMES E IDS DAS LISTAS
lists_in_board = get_lists_in_board(BOARD_ID)

for lista in lists_in_board:
    print(f"Nome da Lista: {lista['name']}, ID da Lista: {lista['id']}")

# Exemplo de impressão dos dados processados
for card_data in processed_data:
    print(f"Nome: {card_data['name']}, Criado em: {card_data['created_at']}")

# funcao responsiva do titulo do html
def add_title(ws, title):
    title_cell = ws.cell(row=1, column=1, value=title)
    title_cell.alignment = Alignment(horizontal='center')
    title_cell.font = Font(bold=True, size=14)
