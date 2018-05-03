import MeCab
import unicodedata

with open('nogizaka_lyric.txt', 'r', encoding='utf-8') as file:
    lyric_text = file.read()

text = unicodedata.normalize('NFKC', str(lyric_text))

mt = MeCab.Tagger("-Ochasen")
tmp_lists = []

with open('nogizaka_text_splited.txt', 'w', encoding='utf-8') as file:
    node = mt.parseToNode(text)
    while node:
        if node.feature.startswith('名詞') or node.feature.startswith('形容詞') or node.feature.startswith('動詞'):
            tmp_lists.append(node.surface)
        node = node.next
    file.write(' '.join(tmp_lists)+'\n')
