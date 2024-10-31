import requests

user = ""
password = ""
sender = ""
receiver = "79997358253"
text = "Hello, world!"

url = f"https://my3.webcom.mobi/sendsms.php?user={user}&pwd={password}&sadr={sender}&dadr={receiver}&text={text}"
print(url)
response = request.get(url)
print(response)
if response.status_code == 200:
    print("Сообщение успешно отправлено")
else:
    print(f"ошибка при отправке {response.status_code}")