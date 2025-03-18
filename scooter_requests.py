import requests
import configuration
import data

def create_order(body): # Создание заказа

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body, headers=data.headers)

def find_order(track): #Поиск заказа

    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_PATH + str(track))
