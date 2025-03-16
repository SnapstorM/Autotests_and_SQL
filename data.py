# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

courier_data = {
    "login": "ninja",
    "password": "1234",
    "firstName": "saske"
}

order_data = {
     "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}