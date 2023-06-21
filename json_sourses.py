import json


def get_jewelry_data():
    with open('texts/jewelry/jewelry_art.json', 'r', encoding='utf-8') as file:
        jewelry_data = json.load(file)
    return jewelry_data
