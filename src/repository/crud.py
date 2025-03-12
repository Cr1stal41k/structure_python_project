import functools

from sqlalchemy.orm import Session

from repository.db_connect import SessionLocal
from repository.models import FilmModel, PersonModel
from repository.schemas import FilmSchema, PersonSchema


def connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with SessionLocal() as session:
            out = func(
                *args,
                **kwargs,
                db=session,
            )
        return out

    return wrapper


@connection
def create_film(films: FilmSchema, db: Session):
    db_model = FilmModel(
        name=films.name,
        actor=films.director,
    )
    # db_model = FilmModel(**films)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


@connection
def create_person(person: PersonSchema, db: Session):
    db_model = PersonModel(
        name=person.name, second_name=person.second_name, number=person.number
    )
    # db_model = PersonModel(**films)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


@connection
def get_persons(db: Session):
    return db.query(PersonModel).all()


@connection
def get_persons_by_name(name: str, db: Session):
    return db.query(PersonModel).filter(PersonModel.name == name).all()


@connection
def update_persons_by_id(id: int, person: PersonSchema, db: Session):
    person_model = db.query(PersonModel).filter(PersonModel.id == id).one()
    person_model.name = person.name
    person_model.second_name = person.second_name
    person_model.number = person.number
    db.commit()
    db.refresh(person_model)


@connection
def delete_persons_by_id(id: int, db: Session):
    db.query(PersonModel).filter(PersonModel.id == id).delete()
    db.commit()
    return db.query(PersonModel).all()
