import MeCab
import unicodedata

with open('Bz_lyric.txt', 'r', encoding='utf-8') as file:
    lyric_text = file.read()

text = unicodedata.normalize('NFKC', str(lyric_text))

textslist = []
textslist = text.splitlines()

mt = MeCab.Tagger("-Ochasen")
tmp_lists = []

with open('Bz_text_splited.txt', 'w', encoding='utf-8') as file:
    for line in textslist:
        node = mt.parseToNode(line)
        while node:
            if node.feature.startswith('名詞') or node.feature.startswith('形容詞') or node.feature.startswith('動詞') and not '非自立' in node.feature:
                tmp_lists.append(node.surface)
            node = node.next
        file.writelines(' '.join(tmp_lists) + '\n')
        tmp_lists = []
