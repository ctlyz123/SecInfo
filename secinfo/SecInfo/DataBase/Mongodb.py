from DataBase.Database import Database
import pymongo

class Mongodb(Database):
    def __init__(self):
        pass
    def connect(self,host='127.0.0.1', port=27017,dbs="",tables=""):
        self.con = pymongo.MongoClient(host=host, port=port)[dbs][tables]
        return self
    def select(self,sql,column={}):
        return self.con.find_one(sql,column)
    def select_all(self,sql,column={}):
        return self.con.find(sql,column)
    def delete(self,sql):
        self.con.delete_one(sql)
    def insert(self,sql):
        self.con.insert_one(sql)
    def update(self,sql,setting):
        self.con.update_one(sql,setting)
    def delete(self,sql):
        self.con.delete_one(sql)