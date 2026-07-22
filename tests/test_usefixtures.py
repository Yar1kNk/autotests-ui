import pytest

@pytest.fixture
def clear_books_databse():
    print("[FIXTURE] Удаляем все данные из базы данных")

@pytest.fixture
def fill_books_databse():
    print("[FIXTURES] Создаем новые данные в базе данных")



@pytest.mark.usefixtures('fill_books_databse')
def test_read_all_books_in_library(self):
    print("Reading all books")

@pytest.mark.usefixtures(
    'clear_books_databse',
    'fill_books_databse',
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...
    def test_delete_book_from_library(self):
        ...