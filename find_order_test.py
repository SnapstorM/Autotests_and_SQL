# Максим Иванов, 27-я когорта - Финальный проект. Инженер по тестированию плюс

import scooter_requests
import data

def test_status_code():

    track = scooter_requests.create_order(data.order_data)
    result = scooter_requests.find_order(track)

    assert result.status_code == 200
