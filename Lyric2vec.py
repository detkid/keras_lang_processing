import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim

from gensim.models import word2vec

sentences = word2vec.LineSentence('nogizaka_text_splited.txt')
model = word2vec.Word2Vec(sentences,
                          sg=1,  # 0: CBOW, 1: skip-gram
                          size=30,     # ベクトルの次元数
                          window=4,    # 入力単語からの最大距離
                          min_count=5,  # 単語の出現回数でフィルタリング
                          )

print(model.most_similar(positive='恋', topn=20))
