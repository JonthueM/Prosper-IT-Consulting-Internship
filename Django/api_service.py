import json
import http.client
import requests


def get_data():
    connection = http.client.HTTPConnection('https://api.rawg.io/api')
    headers = {'User-Agent':'Bootcamp Offline Game App Project', 'From': 'connect@jonthuemichel.com'}
    connection.get('GET','/games', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response

def get_dates():
    connection = http.client.HTTPConnection('https://api.rawg.io/api')
    headers = {'User-Agent':'Bootcamp Offline Game App Project', 'From': 'connect@jonthuemichel.com'}
    connection.get('GET','/games', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response

def get_data():
    connection = http.client.HTTPConnection('https://api.rawg.io/api')
    headers = {'User-Agent':'Bootcamp Offline Game App Project', 'From': 'connect@jonthuemichel.com'}
    connection.get('GET','/games', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response

def get_data():
    connection = http.client.HTTPConnection('https://api.rawg.io/api')
    headers = {'User-Agent':'Bootcamp Offline Game App Project', 'From': 'connect@jonthuemichel.com'}
    connection.get('GET','/games', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response