test_str = 'Geeksforgeeks is best for geeks and CS'
words= test_str.split()
word_list = ["best", 'CS', 'for']
repl_word='gfg'
for i, j in enumerate(words):
    if j in word_list:
        words[i]=repl_word
print(words)

test_str = 'Geeksforgeeks is best for geeks and CS'
test_str2 = 'Geeks for geeks best for geeks CS'
word_list = ["best", 'CS', 'for']
repl_word='gfg'
res=' '.join([repl_word if idx in word_list else idx for idx in test_str.split()])
print(res)
