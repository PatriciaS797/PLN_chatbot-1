import webbrowser
from bs4 import BeautifulSoup
import requests
import os
import openai
import re
from dotenv import load_dotenv
#pip install beautifulsoup4
#pip install python-dotenv
#pip install openai

def playMusic(query):

    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    pattern = r'(/watch\?v=[^"]+)\\'
    matches = re.findall(pattern, response.text)
    # print(matches)
    url = f"https://www.youtube.com/{matches[0]}"+ "&autoplay=1"
    webbrowser.open(url + query, new=2)

if __name__ == "__main__":
    playMusic("khordell")

def getWeather(city,complete):
    load_dotenv()
    # Obtener el valor de la clave de API
    api_key = os.getenv('WEATHER_API1')
    print(api_key)
    url= f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    location_name = data["location"]["name"]
    location_region = data["location"]["region"]
    location_country = data["location"]["country"]
    current_temp_c = data["current"]["temp_c"]
    current_condition_text = data["current"]["condition"]["text"]
    wind_kph = data["current"]["wind_kph"]
   # wind_dir = data["wind_dir"]
   # humidity = data["humidity"]
   # feelslike_c=data["feelslike_c"]
   
    if complete==True :
        res=  f"The current temperature is {current_temp_c} degrees Celsius.It is {current_condition_text} and the wind speed is {wind_kph} km/h."
    else:
        res = f"The current temperature is {current_temp_c} degrees Celsius."
    return res

def getNews():
    load_dotenv()
    # Obtener el valor de la clave de API
    api_key = os.getenv('NEWS_API')
    print(api_key)
    url = f"https://newsapi.org/v2/top-headlines?country=us&sortBy=popularity&pageSize=5&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    print(data["totalResults"])
    print(data["status"])
    titles = []
    for article in data["articles"]:
        titles.append(article["title"])
    return titles

def summarize():
    openai.api_key_path="./.env"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    with open('./ejemplo.txt', 'r') as file:
        contenido = file.read()
    contenido+=contenido + "\n\nTl;dr"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=contenido,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    data = response.json()
    return data
