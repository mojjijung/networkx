import pandas as pd

import re
import kss
from konlpy.tag import Okt
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer


def apply_regular_expression(text):
    hangul = re.compile('[^ ㄱ-ㅣ 가-힣]')  # 한글 추출 규칙: 띄어 쓰기(1 개)를 포함한 한글
    result = hangul.sub('', text)  # 위에 설정한 "hangul"규칙을 "text"에 적용(.sub)시킴
    return result


df = pd.read_csv("raws/test2.csv")
df.head()

print(df.head())
# dimension
df.shape

# information
# df.info()

# text 변수 확인
df['text'][0]
print(df['text'][0])

corpus = "".join(df['text'].tolist())
corpus
# print(corpus)

okt = Okt()  # 명사 형태소 추출 함수
# 정규 표현식 적용
apply_regular_expression(corpus)
nouns = okt.nouns(apply_regular_expression(corpus))

#print(nouns)
tokenizer = apply_regular_expression(corpus)
# # stop_words = stopwords.words('english')
stop_words = pd.read_csv("https://raw.githubusercontent.com/yoonkt200/"
                            + "FastCampusDataset/master/korean_stopwords.txt").values.tolist()
#
count = {} # 동시출현 빈도가 저장될 dict
for line in df['text']:
    # line = line.strip()
    # print(line)
    # tokens = tokenizer.tokenize(line) # 각 리뷰를 토큰화한 뒤 리스트에 저장
    tokens =kss.split_sentences(line)
    # print('tokens' , tokens)
    stopped_tokens = [i for i in list(set(tokens)) if not i in stop_words+["br"]]
    stopped_tokens2 = [i for i in stopped_tokens if len(i)>1]
    # print(tokens)
    for i,a in enumerate(stopped_tokens2):
        for b in stopped_tokens2[i+1:]:
            if a>b:
                count[b,a] = count.get((b,a),0) + 1
            else:
                count[a,b] = count.get((a,b),0) + 1

print(count)