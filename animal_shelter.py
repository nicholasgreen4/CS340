from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

class AnimalShelter(object):
    # CRUD operationsOperation for Animal collection in MongoDB.

    def __init__(self, username: str, password: str, host: str, port: int):
        # Initialize the MongoClient and connect to the specified database and collection
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'aac'
        COL='animals'

        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]


    def create(self, data):
        # Inserts a document into the collection.
        # Args: data (dict): A dictionary representing the document to insert.
        # Returns: bool: True if insert is successful, False otherwise
        if data is None or not isinstance(data, dict):
            raise ValueError("Data must be a non-empty dictionary.")
        try:
            result = self.collection.insert_one(data)
            return result.acknowledged
        except PyMongoError as e:
            print(f"Insert failed: {e}")
            return False

    def read(self, query):
        # Queries for documents from the collection
        # Args: query (dict): A dictionary representing the filter for the find operation.
        # Returns: list A list of documents matching the query
        if query is None or not isinstance(query, dict):
            raise ValueError("Query must be a non-empty dictionary.")

        try:
            documents = list(self.collection.find(query))
            return documents
        except PyMongoError as e:
            print(f"Query failed: {e}")
            return []

    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except PyMongoError as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"Delete errorerror: {e}")
            return 0


