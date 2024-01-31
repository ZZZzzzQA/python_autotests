import requests
import pytest
token = "7e7432b6573a18615f82cd9bb9b9ea9d"

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}


def test_get_trainers():
    #FT-1 GET trainers by level
    response = requests.get(url=f'{URL}/trainers', params={'level':1}, timeout=15)
    assert response.status_code == 200, 'Unexpected status code'
    

def test_get_me():
    #FT-1 GET trainers by level
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':'3744'}, timeout=15)
    assert response != response.json()['trainer_name']=='Джон Рембо' , 'Unexpected'