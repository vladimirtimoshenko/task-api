import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app


@pytest.fixture(autouse=True)
def mock_rag_chain(monkeypatch):
    mock_chain = MagicMock()
    mock_chain.invoke.return_value = "Test answer [1]."

    mock_retriever = MagicMock()
    mock_doc = MagicMock()
    mock_doc.metadata = {"source": "test-source"}
    mock_doc.page_content = "Test context"
    mock_retriever.invoke.return_value = [mock_doc]

    monkeypatch.setattr(
        "app.main.build_rag_chain",
        lambda: (mock_chain, mock_retriever),
    )


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c
