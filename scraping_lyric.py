import requests
from bs4 import BeautifulSoup

artist_url = "https://www.uta-net.com/artist/12550/"
artist_page = requests.get(artist_url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(artist_page.text, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)
