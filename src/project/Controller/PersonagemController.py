from Services.PersonagemService import PersonagemService
import requests


class PersonagemController:
    __personagemService : PersonagemService

    def __init__(self, personagemService):
        self.__personagemService = personagemService

        
    def cadastrarPersonagens(self):
        url = "https://rickandmortyapi.com/api/character/"
        services = self.__personagemService
        try:
            response = requests.get(url)
            response.raise_for_status()  # Levanta um erro se o status não for 200
            data = response.json()
        except requests.exceptions.RequestException as e:
            return {"error": "Erro ao buscar personagem", "details": str(e)}
        services.inserindoDados(data['results'])
