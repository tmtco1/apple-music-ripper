from selenium import webdriver
import time
from bs4 import BeautifulSoup
import config

if len(config.deezer_arl) < 1:
    print("No Deezer ARL found in config.py. You can get one from https://rentry.org/firehawk52#deezer-arls.")
    exit(0)

def get_playlist(url):

    if config.chrome:
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    songs = soup.find_all('div', class_="songs-list-row__song-name")
    songsc = []

    for song in songs:
        songsc.append(song.text)

    return songsc

print(get_playlist(input("Enter Apple Music Playlist Link: ")))
