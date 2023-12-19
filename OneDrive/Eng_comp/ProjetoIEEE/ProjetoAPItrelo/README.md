API_KEY = '805620170833c176f9ee5e544b7942a2'
TOKEN = 'ATTAc0234c9c978a41f7200408c74fed60bbf8e7990678c013cf39bde5ffaa0f5014BA64FCCD'
ID_QUADRO = 'zjjgKBL4'
ID_LISTA = '652f8ef565c24730f6bb1b17'


Nome da Lista: EQUIPES, ID da Lista: 652f8ef565c24730f6bb1b14
Nome da Lista: MAIS URGENTE, ID da Lista: 652f8ef565c24730f6bb1b15        
Nome da Lista: PROJETO EM ANDAMENTO, ID da Lista: 652fb5afa762af73ec36b700
Nome da Lista: PROJETO A INICIAR, ID da Lista: 652f8ef565c24730f6bb1b16   
Nome da Lista: PROJETO EM ESPERA, ID da Lista: 652f8ef565c24730f6bb1b18   
Nome da Lista: PROJETO CONCLUIDOS, ID da Lista: 652f8ef565c24730f6bb1b17 

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