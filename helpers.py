import webbrowser
from bs4 import BeautifulSoup
import requests
import re

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