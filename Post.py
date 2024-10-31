import  requests
import json


url = "https://my3.webcom.mobi/json/balance.php"
headers = {"Content-type": "text/json; charset=utf-8;"}

data = {"login":"Mariya643",
        "password":"818385"}
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