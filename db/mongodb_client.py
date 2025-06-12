from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, db_name: str, collection_name:str):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def insert_one(self, data: dict):
        self.collection.insert_one(data)
    
    def insert_many(self, data: list[dict]):
        self.collection.insert_many(data)
    
    def find_one(self, query: dict):
        return self.collection.find_one(query)