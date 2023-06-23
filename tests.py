# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, add_object):
        # добавляем две книги
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(add_object.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_add_two_books_with_one_name(self, add_object):
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.add_new_book('Гордость и предубеждение и зомби')
        assert len(add_object.get_books_rating()) == 1

    # Нельзя выставить рейтинг книге, которой нет в списке.
    def test_set_book_rating_for_book_which_is_not_in_list(self, add_object):
        add_object.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert not add_object.get_book_rating('Гордость и предубеждение и зомби')

    # Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_book_rating_zero(self, add_object):
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert add_object.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_book_rating_eleven(self, add_object):
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert add_object.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Добавление книги в избранное
    def test_add_book_in_favorites_add_two_books(self, add_object):
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.add_new_book('Что делать, если ваш кот хочет вас убить')
        add_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_object.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(add_object.get_list_of_favorites_books()) == 2

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_which_is_not_in_list_books_rating(self, add_object):
        add_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(add_object.get_list_of_favorites_books()) == 0

    # Проверка удаления книги из избранного
    def test_delete_book_from_favorites_add_two_books_delete_book(self, add_object):
        add_object.add_new_book('Гордость и предубеждение и зомби')
        add_object.add_new_book('Что делать, если ваш кот хочет вас убить')
        add_object.add_book_in_favorites('Гордость и предубеждение и зомби')
        add_object.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        add_object.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(add_object.get_list_of_favorites_books()) == 1

    # У не добавленной книги нет рейтинга.
    def test_add_book_in_favorites_which_is_not_in_list(self, add_object):
        assert not add_object.get_book_rating('Что делать, если ваш кот хочет вас убить')

