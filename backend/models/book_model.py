from bson import ObjectId

class Book:
    def __init__(self, _id=None, book_name=None, isbn=None, author=None, url=None, categories=None):
        self._id = ObjectId(_id) if _id else None
        self.book_name = book_name
        self.isbn = isbn
        self.author = author
        self.url = url
        self.categories = categories

    def to_dict(self):
        return {
            "_id": str(self._id) if self._id else None,
            "book_name": self.book_name,
            "isbn": self.isbn,
            "author": self.author,
            "url": self.url,
            "categories": self.categories
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data.get("_id"),
            book_name=data.get("book_name"),
            isbn=data.get("isbn"),
            author=data.get("author"),
            url=data.get("url"),
            categories=data.get("categories")
        )
