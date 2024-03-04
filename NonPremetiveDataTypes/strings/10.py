# Python – Least Frequent Character in String
test_str = "GeeksforGeeks"
all_freq={}
for ele in test_str:
    if ele in all_freq:
        all_freq[ele]+=1
    else:
        all_freq[ele]=1
print(all_freq)
a={i:j for i,j in all_freq.items() if j==1}
print(min(a))