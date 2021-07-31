import configparser
import requests


def readConfig():
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    return parser


def getApiKey():
    api_key = readConfig()
    return api_key.get("openweathermap", 'api', fallback='No api key was found')


def getUnits():
    units = readConfig()
    return units.get("units", "unit", fallback='No metric unit inserted')


def getWeatherData(city):
    api_key = getApiKey()
    print('this is the api key: {0}'.format(api_key))
    units = getUnits()
    #url = "http://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}".format(city, units, api_key)
    #url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&sys=country&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}"
    data = requests.get(url).json()

    print('from here: {}'. format(data))
    return data

read = readConfig
api = getApiKey()
unit = getUnits()

print('api: {0}'.format(api))

print(unit)

city = 'London'
weather = getWeatherData(city)
print(weather)

import json

aDict = weather
jsonString = json.dumps(aDict)
jsonFile = open("data.json", "a")
jsonFile.write("\n")
jsonFile.write(jsonString)
jsonFile.close()


a_dict = {"a":1, "b":2, "c": 3+2}
values = a_dict.values()
total = sum(values)
print(total)