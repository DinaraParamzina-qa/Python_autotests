import requests
import pytest

#Проверка кода ответа
def test_trainers():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 3988})
    assert response.status_code == 200


    
#Проверка имени тренера
def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 3988})
    assert response.json()['trainer_name'] == 'Princess'