import pytest
from requests_flask_adapter import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app import app
from model.base import Base, db

base_url = "http://127.0.0.1:5000/api/v1/"


@pytest.fixture(autouse=True, scope="session")
def engine():
    engine = create_engine(
        "sqlite:///:memory:",
        isolation_level="READ UNCOMMITTED",
    )
    Base.metadata.create_all(engine)
    db.session.commit()
    return engine


@pytest.fixture(autouse=True, scope="session")
def session_factory(engine):
    return sessionmaker(
        autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
    )


@pytest.fixture(autouse=True, scope="session")
def db_session(session_factory):
    db.session = scoped_session(session_factory)
    return db.session


@pytest.fixture()
def client():
    Session.register("http://localhost", app)
    Session.register("http://localhost:5000", app)
    Session.register("http://127.0.0.1:5000", app)

    return Session()


@pytest.fixture
def post():
    def post_data(client, api_path, payload):
        resp = client.post(url=base_url + api_path, json=payload, headers={})
        return resp

    return post_data


@pytest.fixture
def patch():
    def patch_data(client, api_path, payload):
        resp = client.patch(url=base_url + api_path, json=payload, headers={})
        return resp

    return patch_data


@pytest.fixture
def delete():
    def delete_data(client, api_path):
        resp = client.delete(url=base_url + api_path, headers={})
        return resp

    return delete_data


@pytest.fixture
def get():
    def get_data(client, api_path):
        resp = client.get(url=base_url + api_path, headers={})
        return resp

    return get_data
