import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from repository.crud import (
    create_person,
    delete_persons_by_id,
    get_persons,
    get_persons_by_name,
    update_persons_by_id,
)
from repository.models import Base, PersonModel
from repository.schemas import PersonSchema


@pytest.fixture(scope="session")
def postgres_container():
    with PostgresContainer("postgres:15") as postgres:
        yield postgres

@pytest.fixture(scope="function")
def test_db(postgres_container):
    """Создаем тестовую базу данных и сессию на основе testcontainers."""
    engine = create_engine(postgres_container.get_connection_url())
    os.environ["DB_URL"] = postgres_container.get_connection_url()
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_person(test_db):
    person_data = PersonSchema(name="John", second_name="Doe", number="12345678901")
    new_person = create_person(person_data, db=test_db)
    assert new_person.name == "John"
    assert new_person.second_name == "Doe"
    assert new_person.number == "12345678901"


def test_get_persons(test_db):
    test_create_person(test_db)  # Добавляем данные
    persons = get_persons(db=test_db)
    assert len(persons) == 1
    assert persons[0].name == "John"


def test_get_persons_by_name(test_db):
    test_create_person(test_db)
    persons = get_persons_by_name("John", db=test_db)
    assert len(persons) == 1
    assert persons[0].name == "John"


def test_update_persons_by_id(test_db):
    test_create_person(test_db)
    person = test_db.query(PersonModel).first()
    updated_data = PersonSchema(name="Jane", second_name="Doe", number="98765432100")
    update_persons_by_id(person.id, updated_data, db=test_db)
    updated_person = test_db.query(PersonModel).filter_by(id=person.id).first()
    assert updated_person.name == "Jane"


def test_delete_persons_by_id(test_db):
    test_create_person(test_db)
    person = test_db.query(PersonModel).first()
    delete_persons_by_id(person.id, db=test_db)
    persons = test_db.query(PersonModel).all()
    assert len(persons) == 0
