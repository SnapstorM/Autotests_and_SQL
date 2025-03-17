# Максим Иванов, 27-я когорта - Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

def create_order(body): # Создание заказа

    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)
    track = str(response.json()['track']) # Сохраняем трек-номер в переменную с типом данных "строка"
    return track

def find_order(track): #Поиск заказа

    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_PATH + track)