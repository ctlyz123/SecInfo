import sys
sys.path.append("..")
from flask import Flask, request, jsonify, render_template
from DataBase.Mongodb import Mongodb
# from  collections import OrderedDict
import urllib3
import json
import os
urllib3.disable_warnings()

app = Flask(import_name=__name__,
            static_url_path='',
            static_folder='../Client/dist',
            template_folder='../Client/dist')

config = json.load(open(os.path.join(os.path.dirname(os.getcwd()),"config.json")))
dbsconf = config["Database"]
mongodb = Mongodb().connect(dbsconf["host"], dbsconf["port"], "secinfo", "twitter")
mongodb_trash = Mongodb().connect(dbsconf["host"], dbsconf["port"], "secinfo", "twitter_trash")

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
app.after_request(after_request)



@app.route('/',methods=['POST','GET'])
def index():

    return render_template('index.html')


@app.route('/delete',methods=['POST','GET'])
def delete():
    hash = request.form.get('hash')
    res = mongodb.update({"hash":hash},{"$set":{"flag":1}})
    delete_one = mongodb.select({"hash":hash},{"_id":0})
    mongodb_trash.insert(delete_one)
    mongodb.delete({"hash":hash})
    return show()

@app.route('/show', methods=['POST', 'GET'])
def show():
    a = mongodb.select_all({"flag":0},{"_id":0,"flag":0})
    res = {}
    # temp = OrderedDict()
    for item in a:
        res[item["hash"]] = item
    # items = res.items()
    # items.sort(reverse=True)
    #
    # for item in items:
    #     temp[item[1]["hash"]] = item[1]
    resJson = jsonify(res)

    return resJson

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
