from pymongo import MongoClient
import pandas as pd


class MongoOperation:
    def __init__(self, client_url: str, database_name: str):
        self.client = MongoClient(client_url)
        self.database = self.client[database_name]

    def bulk_insert(self, data: pd.DataFrame, collection_name: str):
        if not data.empty:
            records = data.to_dict(orient="records")
            self.database[collection_name].insert_many(records)

    def find(self, collection_name: str):
        data = list(self.database[collection_name].find())

        if data:
            return pd.DataFrame(data)

        return pd.DataFrame()
    
