import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db):
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db

    # 创建一个测试用户
    from app.auth import hash_password
    from app import crud
    test_user = crud.get_user_by_username(db, "test")
    if test_user is None:
        crud.create_user(db, "test", hash_password("test123"))

    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def auth_headers(client):
    """登录获取 token，返回带 Authorization 的请求头。"""
    response = client.post(
        "/users/token",
        data={"username": "test", "password": "test123"},
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
