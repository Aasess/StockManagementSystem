import requests
import json
import os
from StockManagementSystem.settings import BASE_DIR

def access_token_generate():
    jsonpath = os.path.join(BASE_DIR,'data.json')
    with open(jsonpath) as f:
        data = json.load(f)
        print(data)


    session = requests.Session()
    session.trust_env = False
    res = requests.post(url='http://127.0.0.1:8000/api/gettoken/',data=data)
    token = res.json()

    headers = {
        'Authorization':f'Bearer {token["access"]}'
    }

    return headers