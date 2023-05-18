import webbrowser
from bs4 import BeautifulSoup
import requests
import os
# import openai
import re
from dotenv import load_dotenv
#pip install beautifulsoup4
#pip install python-dotenv
#pip install openai
import subprocess
import os
from dotenv import load_dotenv
import openai

def playMusic(query):

    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    pattern = r'(/watch\?v=[^"]+)\\'
    matches = re.findall(pattern, response.text)
    # print(matches)
    url = f"https://www.youtube.com/{matches[0]}"+ "&autoplay=1"
    webbrowser.open(url + query, new=2)


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

def cocktail():
    load_dotenv()
    # Obtener el valor de la clave de API
    api_key = os.getenv('NINJA_API')
    name = 'bloody mary'
    limit=1
    api_url = 'https://api.api-ninjas.com/v1/cocktail?name={}&limit={}'.format(name, limit)
    response = requests.get(api_url, headers={'X-Api-Key':api_key})
    data = response.json()
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)

def joke():
    load_dotenv()
    # Obtener el valor de la clave de API
    api_key = os.getenv('NINJA_API')
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)

def activity():
    load_dotenv()
    # Obtener el valor de la clave de API
    api_key = os.getenv('NINJA_API')
    api_url = 'https://api.api-ninjas.com/v1/bucketlist'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        print(response.text)
        return response.text["item"]
    else:
        print("Error:", response.status_code, response.text)

def playChess():
    url = "https://reign.gracehopper.xyz/"
    webbrowser.open(url, new=2)

def code():
    subprocess.Popen(['cmd', '/c', 'code'])

def parse_sentences(sentence):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """I need you to tell the user only the most similar sentence of the following ones that are sepated by commas to their original sentence.\
        This are the sentences:play music, what's the time, what's the weather, joke, i'm bored, tell me the news, cocktail, i want to play chess, open visual studio, classify sentiments.\
        Now when the user asks you a sentence you only MUST return the exact sentence of the previous one which is more similar to the users one"""},
        {"role": "system", "content": """I repeat answer ONLY and ONLY with EXACTLY the most similar sentence I DONT NEED an introduction telling me that thats the sentence,\
        this is inside a script if u give me more than the sentence it will crash"""},
        {"role": "user", "content": sentence}
    ],
    temperature=0
    )
    print(completion.choices[0].message["content"])
    return completion.choices[0].message["content"]

def sentiment_classifier(sentence):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": """the user is gonna tell you short sentences i need you to classify them in positive, neutral, or negative and to tell me the 5 principal feelings they gave to you"""},
        # {"role": "system", "content": """I repeat answer ONLY and ONLY with EXACTLY the most similar sentence I DONT NEED an introduction telling me that thats the sentence,\
        # this is inside a script if u give me more than the sentence it will crash"""},
        {"role": "user", "content": sentence}
    ],
    # temperature=0
    )
    print(completion.choices[0].message["content"])
    return completion.choices[0].message["content"]
