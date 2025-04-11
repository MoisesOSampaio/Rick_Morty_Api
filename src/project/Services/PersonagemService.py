from Repository.PersonagemRepository import PersonagemRepository
from Entities.Personagem import Personagem



class PersonagemService:
    __personagemRepository : PersonagemRepository

    def __init__(self, personagemRepository):
        self.__personagemRepository = personagemRepository

    def tratarDados(lista):
        personagem : Personagem
        personagens: list[Personagem] = []
        for elemento in lista:
            personagem = Personagem(int(elemento['id']),elemento['name'],elemento['status'],elemento['species'],elemento['gender'])
            personagens.append(personagem)
        return personagens
    def inserindoDados(self, lista):
        personagens = self.tratarDados(lista)
        self.__personagemRepository.inserir(personagens)