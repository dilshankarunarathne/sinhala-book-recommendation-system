import pymongo
from bson import ObjectId

from models.book_model import Book
from models.user_model import User

# MongoDB connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = 'BooksDB'
mydb = myclient[db_name]

# Check if the database exists
dblist = myclient.list_database_names()
if db_name in dblist:
    print("The database exists.")
else:
    raise Exception("The database connection failed, DB not found!")

# Check if the collections exist
user_collection_name = 'users'
book_collection_name = 'books'

collist = mydb.list_collection_names()
if user_collection_name not in collist:
    raise Exception("User collection doesn't exist in the DB!")
if book_collection_name not in collist:
    raise Exception("Book collection doesn't exist in the DB!")

# Collections
user_collection = mydb[user_collection_name]
book_collection = mydb[book_collection_name]


# User operations
def insert_user(user):
    if isinstance(user, User):
        user_collection.insert_one(user.to_dict())
    else:
        raise TypeError("Expected a User instance")


def update_user(user_id, update_data):
    user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})


def get_user(user_id):
    user_data = user_collection.find_one({"_id": ObjectId(user_id)})
    return User.from_dict(user_data) if user_data else None


# Book operations
def insert_book(book):
    if isinstance(book, Book):
        book_collection.insert_one(book.to_dict())
    else:
        raise TypeError("Expected a Book instance")


def update_book(book_id, update_data):
    book_collection.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})


def get_book(book_id):
    book_data = book_collection.find_one({"_id": ObjectId(book_id)})
    return Book.from_dict(book_data) if book_data else None


def get_book_by_isbn(isbn):
    book_data = book_collection.find_one({"isbn": isbn})
    return Book.from_dict(book_data) if book_data else None
