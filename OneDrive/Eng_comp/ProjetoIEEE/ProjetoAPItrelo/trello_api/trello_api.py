# api_trello.py
import requests
from config import API_KEY, TOKEN

class TrelloAPI:
    """
    Classe para interação com a API do Trello.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe TrelloAPI.
        """
        self.api_key = API_KEY
        self.token = TOKEN
        self.base_url = "https://api.trello.com/1"

    def get_boards(self):
        """
        Obtém a lista de quadros do usuário.

        Returns:
            list: Lista de quadros.
        """
        url = f"{self.base_url}/members/me/boards"
        params = {"key": self.api_key, "token": self.token}
        response = requests.get(url, params=params)
        return response.json()

    def get_lists(self, board_id):
        """
        Obtém a lista de listas em um quadro.

        Args:
            board_id (str): ID do quadro.

        Returns:
            list: Lista de listas.
        """
        url = f"{self.base_url}/boards/{board_id}/lists"
        params = {"key": self.api_key, "token": self.token}
        response = requests.get(url, params=params)
        return response.json()

    def get_cards(self, list_id):
        """
        Obtém a lista de cartões em uma lista.

        Args:
            list_id (str): ID da lista.

        Returns:
            list: Lista de cartões.
        """
        url = f"{self.base_url}/lists/{list_id}/cards"
        params = {"key": self.api_key, "token": self.token}
        response = requests.get(url, params=params)
        return response.json()

# Exemplo de uso
trello_api = TrelloAPI()

# Exemplo de obtenção de quadros
boards = trello_api.get_boards()
print("Quadros:", boards)

# Exemplo de obtenção de listas em um quadro específico
board_id = "coloque_o_id_do_quadro_aqui"
lists = trello_api.get_lists(board_id)
print("Listas:", lists)

# Exemplo de obtenção de cartões em uma lista específica
list_id = "coloque_o_id_da_lista_aqui"
cards = trello_api.get_cards(list_id)
print("Cartões:", cards)
