#COD PARA PEGAR NOMES E IDS DAS LISTAS
lists_in_board = get_lists_in_board(BOARD_ID)

for lista in lists_in_board:
    print(f"Nome da Lista: {lista['name']}, ID da Lista: {lista['id']}")

# Exemplo de impressão dos dados processados
for card_data in processed_data:
    print(f"Nome: {card_data['name']}, Criado em: {card_data['created_at']}")


