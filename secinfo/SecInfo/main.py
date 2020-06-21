import json
import os
import utils
import search
from hashlib import md5
from DataBase.Mongodb import Mongodb

PATH = os.path.dirname(__file__)
config = json.load(open(os.path.join(PATH,"config.json")))
SearchClass = utils.SearchClass



def main_func():
    dbsconf = config["Database"]
    mongodb = Mongodb().connect(dbsconf["host"],dbsconf["port"],"secinfo","twitter")
    mongodb.con.create_index("hash", unique=True)
    for item in SearchClass:
        res = SearchClass[item]().Search("cve and -")
        for single in res:
            single["hash"] = md5(single["content"].encode("utf-8")).hexdigest()
            single["flag"] = 0
            try:
                mongodb.insert(single)
            except:
                pass

if __name__ == '__main__':
    main_func()