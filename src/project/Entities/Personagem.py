from sqlalchemy.orm import registry, Mapped, mapped_column
from Database.config import table_registry


@table_registry.mapped_as_dataclass
class Personagem:
    __tablename__ = "personagens"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_personagem: Mapped[int]
    nome: Mapped[str]
    status: Mapped[str]
    especie: Mapped[str]
    genero: Mapped[str]

    def __init__(self,id,nome,status,especie,genero):
        self.id_personagem = id
        self.nome = nome
        self.genero = genero
        self.especie = especie
        self.status = status