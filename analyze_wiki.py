from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('./wiki_wakati_utf-8.txt')

# with open('wiki_wakati.txt', 'r', encoding='ISO-8859-1') as file:
#     sentences = file.read()

# text = unicodedata.normalize('NFKC', str(lyric_text))
model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
model.save("./wiki.model")