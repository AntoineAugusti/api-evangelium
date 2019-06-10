import requests
import json
import os
import datetime

BASE_URL = "https://publication.evangelizo.ws/"
date = datetime.date.today()

today_readings = {}

modes = [
    ('data/es/', BASE_URL + 'SP/' + 'days/'),
    ('data/en/', BASE_URL + 'AM/' + 'days/'),
    ('data/it/', BASE_URL + 'IT/' + 'days/'),
    ('data/fr/', BASE_URL + 'FR/' + 'days/'),
    ('data/de/', BASE_URL + 'DE/' + 'days/'),
    ('data/kr/', BASE_URL + 'KR/' + 'days/'),
    ('data/pt/', BASE_URL + 'PT/' + 'days/')
]

for mode in modes:
    base_path, url = mode
    os.makedirs(base_path, exist_ok=True)

    for i in range(7):
        r = requests.get(url + str(date) + "/readings")
        print("Requesting... " + url + str(date) + "/readings")

        data = r.json()

        for j in range(3):

            title = (
                data["data"][j]["book"]["full_title"]
                + " "
                + data["data"][j]["reference_displayed"]
            )

            text = data["data"][j]["text"]
            today_readings[j] = {"title": title, "text": text}

            filename = base_path + str(date) + '.json'

        with open(filename, "w") as f:
            json.dump(today_readings, f, ensure_ascii=False)

        date += datetime.timedelta(days=1)

        print("i is: " + str(i))

        if i == 6:
            date = datetime.date.today()

    





