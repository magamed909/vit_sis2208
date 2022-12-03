import requests
city = "Moscow,RU"
appid = "19d76dd6b19d27529a9a09acca956b55"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print()
    print("Дата <", i['dt_txt'], "> \r\nВидимость <",'{0:+3.0f}'.format(i['visibility']),"m" "> \r\nСкорость ветра <",i['wind']["speed"], "m/s >")
