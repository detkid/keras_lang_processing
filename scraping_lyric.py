import requests
import lxml.html

artist_url = "https://www.uta-net.com/artist/12550/"
artist_page = requests.get(artist_url)

dom = lxml.html.fromstring(artist_page.text)
print(dom.xpath('//*[@id="artist"]//table/tbody//td[@class="side td1"]/a[1]/@href'))
