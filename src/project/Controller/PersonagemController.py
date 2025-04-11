from Services.PersonagemService import PersonagemService
from classes.Request import Request


class PersonagemController:
    __personagemService : PersonagemService

    def __init__(self, personagemService):
        self.__personagemService = personagemService

        
    def cadastrarPersonagens(self):
        services = self.__personagemService
        data = Request.getData()
        services.inserindoDados(data['results'])
