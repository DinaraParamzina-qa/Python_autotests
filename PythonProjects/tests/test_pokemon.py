import requests
import pytest

token = '13a8a8f5db5cf473fcf5d631a53042ec'
#Проверка статуса тренера
def test_trainers():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 3988})
    assert response.status_code ==200

#Проверка имени тренера
def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 3988})
    assert response.json()['trainer_name'] == 'Princess'