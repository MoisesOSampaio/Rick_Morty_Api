from Database.config import session
from Entities.Personagem import Personagem
from sqlalchemy.exc import SQLAlchemyError


class PersonagemRepository:
    def inserir(personagens : list[Personagem]):
        for personagem in personagens:
            session.add(personagem)
        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Erro na inserção dos dados {e}")
        finally:
            session.close()
