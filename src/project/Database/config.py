from sqlalchemy import create_engine
from sqlalchemy.orm import registry, Session

#cria a conexão com o banco de dados
engine = create_engine('sqlite:///src/project/database.db') 
session = Session(engine)
table_registry = registry()