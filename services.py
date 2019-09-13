import json
import requests


def get_weather(api_key, api_url, city):
    api_key = api_key
    api_url = api_url + api_key
    query_url = api_url.format(city)
    try:
        uh = requests.get(query_url)
        data = uh.content
        parsed = json.loads(data)
        weather = None
        if parsed.get("weather"):
            url = "http://openweathermap.org/img/w/"
            icon_url = url + parsed["weather"][0]["icon"]+".png"
            weather = {
                "name": parsed["name"],
                "temperature": str(parsed["main"]["temp"]),
                "symbol": icon_url,
                "description": parsed["weather"][0]["description"],
                "min": str(parsed["main"]["temp_min"]),
                "max": str(parsed["main"]["temp_max"]),
                "hum": str(parsed["main"]["humidity"]),
                "pressure": str(parsed["main"]["pressure"])}
        else:
            weather = {
                "name": "No weather",
                "temperature": "0",
                "symbol": "https://openweathermap.org/img/w/10d.png",
                "description": "Error",
                "min": "0",
                "max": "0",
                "hum": "0",
                "pressure": "0"}
        return weather
    except:
        weather = {
            "name": "Error request",
            "temperature": "0",
            "symbol": "https://openweathermap.org/img/w/10d.png",
            "description": "Error",
            "min": "0",
            "max": "0",
            "hum": "0",
            "pressure": "0"}
        return weather
