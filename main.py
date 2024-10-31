import requests
import re
import json

def check_balance(login, password):
    url = "https://my3.webcom.mobi/json/balance.php"
    headers = {"Content-type": "text/json; charset=utf-8;"}

    data = {"login": login,
            "password":password}
    try:
        response = requests.post(url, data=json.dumps(data), headers = headers)

        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            print(f"Баланс: {response_data["money"]} руб.")
        else:
            print(f"Произошла ошибка {response.status_code}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка {e}")

def validate_phone_number(phone_number):
    pattern = r"^79\d{9}$"
    return bool(re.match(pattern, phone_number))

user = "Mariya643"
password = "818385"
sender = "Mariya"
receiver = "79997358253"
text = "Hello, world!"

balance = check_balance(user, password)
if balance:
    if balance > 10:
        if not validate_phone_number(receiver):
            print("Ошибка неккоректный номер телефона")
        else:
            url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
            print(url)
            try:
                response = requests.get(url)
                print(response)
                if response.status_code == 200:
                    print("Сообщение успешно отправлено")
                else:
                    print(f"ошибка при отправке {response.status_code}")
            except Exception as e:
                print(f"Непредвиденная ошибка с кодом {e}")
    else:
        print("Недостаточно средств!")
else:
    print("Неудалось получить информацию о балансе!")