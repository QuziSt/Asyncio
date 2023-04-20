from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

PG_DSN = 'postgresql+asyncpg://postgres:postgres@127.0.0.1:5431/my_db'
engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class SwapiPeople(Base):
    
    __tablename__ = 'people'
    
    id = Column(Integer, primary_key=True)
    birth_year = Column(String, )
    eye_color = Column(String, )
    films = Column(String, )
    gender = Column(String, )
    hair_color = Column(String, )
    height = Column(String, )
    homeworld = Column(String, )
    mass = Column(String, )
    name = Column(String, )
    skin_color = Column(String, )
    species = Column(String, )
    starships = Column(String, )
    vehicles = Column(String, )

