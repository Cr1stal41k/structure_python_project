# Добавляем скачанные библиотеки
from sqlalchemy import (CHAR, VARCHAR, Column, ForeignKey, Integer,
                        UniqueConstraint)
from sqlalchemy.orm import backref, relationship

from repository.db_connect import Base, create_tables


class PersonModel(Base):
    __tablename__ = 'person'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(20))
    second_name = Column(VARCHAR(20))
    number = Column(CHAR(11), unique=True)
    film = relationship(
        'FilmModel', backref='PersonModel', cascade='all,delete'
    )


class FilmModel(Base):
    __tablename__ = 'film'
    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(20))
    director = Column(
        Integer, ForeignKey('person.id', ondelete='CASCADE'), nullable=False
    )
    person = relationship(
        'PersonModel', backref=backref('FilmModel', cascade='all,delete')
    )
    # __table_args__ = (UniqueConstraint('name', 'actor', name='unique_actor_film'), )


create_tables()
