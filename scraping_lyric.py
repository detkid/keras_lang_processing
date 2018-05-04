import requests
import lxml.html
import pickle

basic_url = "https://www.uta-net.com"

# 乃木坂 https://www.uta-net.com/artist/12550/
# B'z https://www.uta-net.com/artist/134/ https://www.uta-net.com/artist/134/0/2/
artist_url = "https://www.uta-net.com/artist/134/0/2/"
artist_page = requests.get(artist_url)

song_url_list = []
dom = lxml.html.fromstring(artist_page.text)
song_url_list = dom.xpath(
    '//*[@id="artist"]//table/tbody//td[@class="side td1"]/a[1]/@href')

lyrics = []

for song in song_url_list:
    lyric_url = basic_url + song
    lyric_page = requests.get(lyric_url)
    dom2 = lxml.html.fromstring(lyric_page.text)
    lyric = dom2.xpath("//*[@id='kashi_area']/text()")

    song_lyric = ''
    for line in lyric:
        song_lyric = song_lyric + line

    lyric_deleted_space = song_lyric.replace('\u3000', ' ')

    lyrics.append(lyric_deleted_space)

with open('Bz_lyric2.txt', 'w', encoding='utf-8') as file:
    file.writelines("\n".join(lyrics))

# with open('nogizaka_lyric.txt', 'rb') as file:
#     a = pickle.load(file)

print('end')
