import requests

def get_api_url():
    url = 'https://opentdb.com/api.php?amount=50&type=boolean'
    return url

def get_session_token():
    url = 'https://opentdb.com/api_token.php?command=request'
    data = requests.get(url)
    data = data.json()
    token = data['token']
    return token

