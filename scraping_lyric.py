import requests
import lxml.html

basic_url = "https://www.uta-net.com"

artist_url = "https://www.uta-net.com/artist/12550/"
artist_page = requests.get(artist_url)

song_url_list = []
dom = lxml.html.fromstring(artist_page.text)
song_url_list = dom.xpath('//*[@id="artist"]//table/tbody//td[@class="side td1"]/a[1]/@href')

lyrics = []

for song in song_url_list:
    lyric_url = basic_url + song
    lyric_page = requests.get(lyric_url)
    dom2 = lxml.html.fromstring(lyric_page.text) 
    lyric = dom2.xpath("//*[@id='kashi_area']/text()")

    lyrics.append(lyric)

print('end')


