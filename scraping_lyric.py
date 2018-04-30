import requests
from bs4 import BeautifulSoup

URL = "http://www.nikkei.com/"

resp = requests.get(URL)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(resp.text, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)
