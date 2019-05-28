from flask import Flask
from flask import request
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from flask import jsonify
from flask_sslify import SSLify
import requests
import json


app = Flask(__name__)
SSLify = SSLify(app)


URL = 'https://api.telegram.org/bot850923986:AAEoP6rdCMRC2w4JQv5lfQ-tFxd2JiFsV6g/'

"""
def write_json(r, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
"""

def get_json_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'5000',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b0533756-6967-4189-8103-54958facfcfe',
    }
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      json_ob = json.loads(response.text)
      return json_ob
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)


def workable_data(json_ob):
    data = json_ob['data']
    #write_json(data, filename='coinmarketcap2.json')
    return data


def make_dickt(data):
    dict = {}
    for i in data:
        name = i["name"]
        price = i['quote']['USD']['price']
        name_price = {name : price}
        dict.update(name_price)
        #write_json(dict, filename='name_&_price.json')
    return dict


def parse_dict(dict, message):
    price = dict.get(message)
    return price


def send_message(chat_id, text):
    url = URL+'sendMessage'
    answer = {'chat_id':chat_id, 'text':text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        json_ob = get_json_data()
        data = workable_data(json_ob)
        dict = make_dickt(data)
        price = parse_dict(dict, message)
        send_message(chat_id, text=price)

        #write_json(r)
        return jsonify(r)
    return '<h1>Test flask app</h1>'




if __name__ == '__main__':
    app.run()
