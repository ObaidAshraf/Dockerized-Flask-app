import requests
import json
import math

appID = "9091474cf868ce9402862c7bdb9ef6f7"

def getCityWeather(cityName):
    URL = "http://api.openweathermap.org/data/2.5/forecast?q=" + cityName + "&mode=json&appid=" + appID
    r = requests.get(url = URL)
    data = r.json()

    reason = data['cod']
    if (reason == "200"):
        tempK = data['list'][0]['main']['temp']
        tempC = str(math.floor(int(tempK) - 273.15)) + " deg Centigrade"

        weather = data['list'][0]['weather'][0]['description']

        wind = str(data['list'][0]['wind']['speed']) + " meter/sec"

        report = json.dumps({"weather": weather, "temperature": tempC, "wind": wind})
        return (report)
    else:
        errorMsg = data['message']
        hint = "For city like 'New York' provide 'New York' instead of 'NewYork'"
        report = json.dumps({"message": errorMsg, "hint": hint})
        return (report)
