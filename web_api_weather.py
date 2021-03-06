import json
import requests


base_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city={city}'

city_id = '460010'

url = base_url.format(city=city_id)
res = requests.get(url)

res.raise_for_status()

data = json.loads(res.text)
print(data)

print("**** Weather Information@Kagoshima ****")
print("[TIME]")
print(data["description"]["publicTime"])
print("[INFOMATION]")
print(data["description"]["text"])
print("[FORECASTS]")
for i in range(3):
    print("DATE:{} / {}".format(data["forecasts"]
                                [i]["date"], data["forecasts"][i]["telop"]))
