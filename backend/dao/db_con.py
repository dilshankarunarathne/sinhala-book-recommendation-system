import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db_name = 'BooksDB'

mydb = myclient[db_name]

dblist = myclient.list_database_names()
if db_name in dblist:
    print("The database exists.")
else:
    raise Exception("The database connection failed, DB not found!")

collection_name = 'books'
collist = mydb.list_collection_names()
if collection_name in collist:
    print("The collection exists.")
else:
    raise Exception("Collection doesn't exist in the DB!")
