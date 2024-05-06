def compress(string):
    char_freq={}
    for i in string:
        char_freq[i]= char_freq.get(i,0)+1
    new_str=''.join(str(i) + str(j) for i, j in char_freq.items())
    return new_str

s='aabbbccddddeeeeeff'
print(compress(s))