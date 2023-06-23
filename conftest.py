import pytest
from main import BooksCollector


@pytest.fixture
def add_object():
    collector = BooksCollector()
    return collector
