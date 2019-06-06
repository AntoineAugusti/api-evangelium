import requests
import json
import datetime

base_url = "https://publication.evangelizo.ws/"
lang = "SP"
date = "2019-05-09"

dt = datetime.date.today().weekday()
print(dt)

r = requests.get(base_url + lang + "/days/" + date + "/readings")

data = r.json()

today_readings = {}

for i in range(3):
    title = (
        data["data"][i]["book"]["full_title"]
        + " "
        + data["data"][i]["reference_displayed"]
    )
    text = data["data"][i]["text"]
    today_readings[i] = {"title": title, "text": text}


filename = "test.json"
with open(filename, "w") as f:
    json.dump(today_readings, f, ensure_ascii=False)
