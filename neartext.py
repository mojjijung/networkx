import pandas as pd

f= open('raws/b10bu.txt', encoding='UTF8')
lines = f.readlines()
# len(lines)
# print(len(lines))

lines

words_list=[]

for text in lines:
    words_list.append(text.strip())

print(words_list[1])
# 불용어처리
stopwords =[]
f =open('raws/stopwords.txt')
lines = f.readlines()
for line in lines:
    line = line.strip()
    stopwords.append(line)
f.close()
# 불용어 list 만들어 줌

print('불용어 사전 출력' ,stopwords)



count = {}
for line in words_list:
    words = list(set(line.split()))

    # print(words)

    for i,a in enumerate(words):
        print('i의 값 : ' ,i ,' a의 값 : ' , a)

        for b in words[i+1:]:
            if b not in stopwords:
                if a>b:
                    count[b,a] = count.get((b,a),0) +1
                else:
                    count[a,b] = count.get((a, b), 0) + 1

# print(count)

count.get(("a","b"),0)
# print(count)
df=pd.DataFrame.from_dict(count, orient='index')
df.head
# print(df.head)

list1=[]
for i in range(len(df)):
    list1.append([df.index[i][0], df.index[i][1], df[0][i]])

df2= pd.DataFrame(list1, columns=["term1","term2","freq"])

# print(df2)

df3=df2.sort_values(by=['freq'],ascending=False)
df3.head(10)

print(df3.head(10))