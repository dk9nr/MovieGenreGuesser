#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
  
URL = "https://www.tunefind.com/movie/joker-2019"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
s  =soup.find_all("a", class_ = "SongTitle__link___2OQHD")
songs = []
for elem in s:
#     # wrappers = elem.find_all('div')
#     # for x in wrappers:
    # title = elem.select('a')['title']
    # title  =soup.find_all("a", class_ = "SongTitle__link___2OQHD")
    # print(elem['title'])
    # try:
    #     text = elem.find('a').get_text() 
    # except AttributeError:
    #     text = None
    songs.append(elem['title'])
    
    # print(text) 
for song in songs:
    song = list(song)
    urlstring = ''
    titlelength = len(song)
    for word in song:
        if word == ' ':
            urlstring += '+'
        else:
            urlstring += word
    url = 'https://www.discogs.com/search/?q='+urlstring+'&type=all'
    r2 = requests.get(url) 
  
    soup2 = BeautifulSoup(r2.content, 'html5lib') 
    s2  =soup2.find("div",class_='card card_large float_fix shortcut_navigable')
    print(s2)
    # for elem in s2:
    #     cur=elem.find("h4")
    #     print(cur)
        
    # print('STARTING HERE: ',urlstring)


    




