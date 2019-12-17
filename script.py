#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 

movie = input('Which movie?\n')
year = input('Which year?\n')

URL = 'https://www.tunefind.com/movie/'+ movie+',-'+year
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
import re
genreurls = set()
sg = {}
for song in songs:
    orig = song
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
    # print(s2)
    if not s2:
        continue
    for elem in s2:
        a  =s2.find("a", class_="search_result_title")
        # print(a['href'])
        genreurls.add(a['href'])
        # name = " ".join(song)
        sg[a['href']] = orig
        break
        
    # for elem in s2:
    #     cur=elem.find("h4")
    #     print(cur)

    # print('STARTING HERE: ',urlstring)
    
    # song genre page

d = {}
g = {}
for genreurl in genreurls:
    fullURL = 'http://discogs.com'+genreurl
    r3 = requests.get(fullURL) 
    soup3 = BeautifulSoup(r3.content, 'html5lib')
    s3  =soup3.find("div",class_='profile')
    for elem in s3:
        content = soup3.find("div",class_='content')
        try:
            for elem2 in content:
                # print(type(elem2))
                if elem2.name == 'a':
                    if elem2['href'].startswith('/genre/'):
                        genre = elem2.get_text()
                        if genre in g:
                            g[genre] += 1
                        else:
                            g[genre] = 1
                        if genre in d:
                            d[genre].append(sg[genreurl])
                        else:
                            d[genre] = [sg[genreurl]]
                    
                    
                    # print(elem2.get_text())
        except:
            continue
        break
print('Genre Counts: ')
for i in g:
    print(i,': ', g[i])
print('-------------------------------')
print('Songs in Each Genre')
for i in d:
    print(i, ': ')
    for j in d[i]:
        print(j)
    print('-------------------------------')

 


    




