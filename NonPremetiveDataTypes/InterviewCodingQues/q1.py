def freq_words():
    str_='sheena loves eating apple and her sister too loves eating apple'
    str_split=str_.split()
    d={}
    for i in str_split:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    duplicate_words={i:j for i,j in d.items() if j>1}
    a=[i for i, j in duplicate_words.items()]
    return a
x=freq_words()
print(x)