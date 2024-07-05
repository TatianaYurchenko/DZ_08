import urllib.request
import json
# получение интернет данных
# для этого необходимо импортировать библиотеку urllib.request

def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    print("result code:" + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        print(data)
    else:
        print("error")

def printResults():
    # use json modul to load the string data into a dictionary
    # ссылка на json https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    # Использовать для того чтобы понимать как выглядит json, чтобы вытягивать из него данные
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl = urllib.request.urlopen(urlData)
    data = webUrl.read()
    theJson = json.loads(data)
    # access the contents of the JSON
    if "title" in theJson["metadata"]:
        print(theJson["metadata"]["title"])
    count = theJson["metadata"]["count"]
    print(count)
    # for i in theJson["features"]:
    #     print(i["properties"]["place"])
    # print("----------\n")
    for i in theJson["features"]:
        if i["properties"]["mag"] >= 4:
            print(i["properties"]["place"])
    print("----------\n")

printResults()
