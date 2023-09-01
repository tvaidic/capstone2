from base import Base
from dotenv import load_dotenv
import pymongo
import os

class ToMongo(Base):
    def __init__(self):
        Base.__init__(self)
        load_dotenv()
        self.user = os.getenv('USER')
        self.password = os.getenv('PASS')
        self.mongo_url = f'mongodb+srv://{self.user}:{self.password}@cluster0.qpyltsb.mongodb.net/?retryWrites=true&w=majority'
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client.db 
        self.weapons = self.db.weapons
        self.df.set_index('id',inplace=True)

    def upload_one_by_one(self):
        self.weapons.drop()

        Base.__init__(self)
        for i in self.df.index:
            self.weapons.insert_one(self.df.loc[i].to_dict())
if __name__ == '__main__':
    c = ToMongo()
    c.upload_one_by_one()