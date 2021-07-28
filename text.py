from krwordrank.word import KRWordRank
from krwordrank.hangle import normalize

min_count = 5   # 단어의 최소 출현 빈도수 (그래프 생성 시)
max_length = 10 # 단어의 최대 길이
verbose =True
wordrank_extractor = KRWordRank(min_count, max_length , verbose)

beta = 0.85    # PageRank의 decaying factor beta
max_iter = 10

with open('raws/b10bu.txt', 'r') as f:
    texts = []
    for line in f:
        texts.append(line)

texts = [normalize(text,english=False , number=True) for text in texts ]
keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter)
#
for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:30]:
        print('%8s:\t%.4f' % (word, r))
#
from krwordrank.word import summarize_with_keywords
#
stopwords ={'제거','할','단어'}
keywords = summarize_with_keywords(texts, min_count=5, max_length=10,
    beta=0.85, max_iter=10, stopwords=stopwords, verbose=True)
keywords = summarize_with_keywords(texts) # with default arguments
print(keywords)