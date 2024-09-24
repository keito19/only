import requests
import pytest

url = "https://api.only.digital/api/ru/brief"
headers = {
    "accept": "application/json",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "authorization": "0948081941de9b3cdead5e570118cbe30da14398f64bfa3556b6bd14e6d24416",
    "origin": "https://only.digital",
    "priority": "u=1, i",
    "referer": "https://only.digital/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}


# отправка правильно заполненной формы
def test_1():

    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без заполненного имени
def test_21():

    payload = {
        "name": "",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод имени с пробелом в начале
def test_22():
    payload = {
        "name": " ",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод цифр в поле имени
def test_23():
    payload = {
        "name": "23423",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод спецсимволов в поле имени
def test_24():
    payload = {
        "name": "$%^",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод номера, состоящего из 9 цифр
def test_31():
    payload = {
        "name": "dsfsdfsd",
        "phone": "789635480",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод номера, состоящего из 12 цифр
def test_32():
    payload = {
        "name": "dsfsdfsd",
        "phone": "794735384021",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без заполненного телефона
def test_33():
    payload = {
        "name": "dsfsdfsd",
        "phone": "",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод текста вместо номера
def test_34():
    payload = {
        "name": "dsfsdfsd",
        "phone": "аавымапыпаваы",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод спецсимволов вместо номера
def test_35():
    payload = {
        "name": "dsfsdfsd",
        "phone": "$%^",
        "email": "dfdfd@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без заполненного емейла
def test_41():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы с невалидным емейлом (две собачки)
def test_42():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "df@dfd@gmail.com",
        "company": "fddfgdgf",
        "description": "",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод емейла с несуществующим доменом
def test_43():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "sdfsdf@ggg.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод емейла с недопустимыми  символами
def test_44():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "sdfdf%^&sf@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод кириллицы в поле емейла
def test_45():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "лватовпв@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод емейла без точек в домене
def test_46():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "fdfgdgfdg@yandexru",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# ввод емейла с пробелом в начале
def test_47():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": " dfdgdg@gmail.com",
        "company": "sdfdfsdf",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без заполненного названия компании
def test_5():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "",
        "description": "dsffdds",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без заполненного описания
def test_6():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "fddfgdgf",
        "description": "",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без выбранного бюджета
def test_7():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "erwrerwe",
        "description": "dsffdds",
        "budget": "",
        "recommendation": "Копирайт на сайте",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без выбранной рекомендации
def test_8():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "fddfgdgf",
        "description": "",
        "budget": "Менее 2 млн",
        "recommendation": "",
        "type": "Сайт",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


# отправка формы без выбранного типа
def test_9():
    payload = {
        "name": "dsfsdfsd",
        "phone": "72342322322",
        "email": "dfdfd@gmail.com",
        "company": "fddfgdgf",
        "description": "",
        "budget": "Менее 2 млн",
        "recommendation": "Копирайт на сайте",
        "type": "",
    }

    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
