from pymongo import MongoClient


class CRUD:
    def __init__(self, username, password, database):
        uri = f"mongodb://{username}:{password}@localhost:27017/{database}?authSource=AAC"
        try:
            self.client = MongoClient(uri)
            self.db = self.client[database]
            print("Connected to MongoDB successfully.")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
    
    def read(self, query):
        try:
            collection = self.db["animals"]
            results = collection.find(query)
            data = [result for result in results]  
            print(f"Data retrieved from MongoDB: {data}")
            return data
        except Exception as e:
            print(f"Error retrieving data from MongoDB: {e}")
            return []
