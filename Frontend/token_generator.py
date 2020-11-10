import requests


def access_token_generate():
    data = {
        'username':'ashish',
        'password':'1234'
    }
    session = requests.Session()
    session.trust_env = False
    res = requests.post(url='http://127.0.0.1:8000/api/gettoken/',data=data)
    token = res.json()

    headers = {
        'Authorization':f'Bearer {token["access"]}'
    }

    return headers