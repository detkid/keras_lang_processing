import MeCab

text = "私はバナナが好きです。"

mecabTagger = MeCab.Tagger("-Ochasen")
node = mecabTagger.parseToNode(text)
while node:
    word = node.surface
    hinshi = node.feature.split(",")[0]
    print(word+": "+hinshi)
    node = node.next