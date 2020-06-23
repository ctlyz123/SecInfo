import json
import os
import utils
import search
from hashlib import md5
from DataBase.Mongodb import Mongodb
from  collections import OrderedDict

PATH = os.path.dirname(__file__)
config = json.load(open(os.path.join(PATH,"config.json")))
SearchClass = utils.SearchClass

cache = OrderedDict()



def check_cache(hash):
    if not cache.has_key(hash) :
        if len(cache) == 100:
            cache.pop(cache.keys()[0])
        cache[hash] = 1
        return True

    else:
        return False
def load_cache():
    global cache
    if os.path.exists(config['cache']['filename']):
        with open(config['cache']['filename'], 'r') as f:
            cache = OrderedDict(**json.load(f))

def save_cache():
    with open(config['cache']['filename'],'w') as f:
        return json.dump(cache,f)

def main_func():
    load_cache()
    dbsconf = config["Database"]
    mongodb = Mongodb().connect(dbsconf["host"],dbsconf["port"],"secinfo","twitter")
    mongodb.con.create_index("hash", unique=True)
    for item in SearchClass:
        res = SearchClass[item]().Search("cve and -")
        for single in res:
            single["hash"] = md5(single["content"].encode("utf-8")).hexdigest()
            single["flag"] = 0

            try:
                if check_cache(single["hash"]) :
                    mongodb.insert(single)
            except:
                pass

    save_cache()

if __name__ == '__main__':
    main_func()