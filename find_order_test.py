# Максим Иванов, 27-я когорта - Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data

def create_order(body): # Создание заказа

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)

def find_order(): #Проверка статуса
    
    # Трек-номер перевожу в строку и методом конкатенации присоединяю к URL
    response = requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_PATH + str(create_order(data.order_data).json()['track']))

    assert response.status_code == 200 # Проверка статуса заказа
    print("Тест пройден!") # Выводится в случае, если статус заказа - 200

find_order()
