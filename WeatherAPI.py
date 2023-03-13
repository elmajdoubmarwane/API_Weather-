import requests , json 

URL_BASE = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "q": "Wels,AT", 
    "appid" : "006a11dbf445f7a7f53df5b2a7c9d946",
    "units" : "metric" #specifying the unit Celcuis of temperature
}

response = requests.get(URL_BASE, params = parameters)
if (response.status_code == 200):
    # extract the data in a json form 
    data = response.json()
    # specify the information to extract
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    rain = data.get("rain",{}).get("1h")
    cloud = data.get("clouds",{}).get("all")

    # show up the information
    print(f"WELS Weather\n Temperature = {temp:.1f}°C\n Wind = {wind} m/s\n Rain = {rain}\n Cloud = {cloud}\n Humidity = {humidity}%")

else:
    print("ERROR")








