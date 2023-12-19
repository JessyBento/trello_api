# trello_api/trello_api.py

import requests

class TrelloAPI:
    """
    Classe para interação com a API do Trello.
    """

    def __init__(self, api_key, token):
        """
        Inicializa uma nova instância da classe TrelloAPI.

        Args:
            api_key (str): ''
            token (str): ''
        """
        self.api_key = api_key
        self.token = token
        
        self.base_url = "https://api.trello.com/1"

    def get_boards(self):
        """
        Obtém a lista de quadros do usuário.

        Returns:
            list: Lista de quadros.
        """
        # Implementação...

    def get_lists(self, board_id):
        """
        Obtém a lista de listas em um quadro.

        Args:
            board_id (str): ID do quadro.

        Returns:
            list: Lista de listas.
        """
        # Implementação...

    def get_cards(self, list_id):
        """
        Obtém a lista de cartões em uma lista.

        Args:
            list_id (str): ID da lista.

        Returns:
            list: Lista de cartões.
        """
        # Implementação...
