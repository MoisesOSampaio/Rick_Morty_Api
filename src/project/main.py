from Controller.PersonagemController import PersonagemController
from Services.PersonagemService import PersonagemService
from Repository.PersonagemRepository import PersonagemRepository


Controller = PersonagemController(PersonagemService(PersonagemRepository))
Controller.cadastrarPersonagens()





