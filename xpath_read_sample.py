import lxml.html

html = open('sample.html', encoding='utf-8').read()
dom = lxml.html.fromstring(html)

print(dom.xpath('normalize-space(//h1[@class="siteTitle"])'))
