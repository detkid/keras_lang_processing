# keras_lang_processing

## HowtoUse

1. スクレイピング等でテキストデータを取得

    scraping_lyric.pyで歌詞データを取得

1. 取得したテキストデータを形態素解析で分かち書き
    
    analyze_lyric.pyでMeCabで名詞、動詞などを抽出して分かち書き

1. word2vecのモデル構築
    
    lyric2vec.pyでkeras/gensimモデルを構築
