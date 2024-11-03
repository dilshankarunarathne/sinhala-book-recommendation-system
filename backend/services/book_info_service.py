from dao.db_con import get_book_by_isbn


def get_info(isbn: str):
    return get_book_by_isbn(isbn)
