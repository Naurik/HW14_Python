import requests

req = requests.get('https://habrahabr.ru/')
page = req.text

