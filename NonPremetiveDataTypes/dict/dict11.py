input = 'ant magenta magnate tan gnamate'
anagram_dict={}

try:
    for ele in input.split():
        key= ''.join(sorted(ele))
        if key in anagram_dict.keys():
            anagram_dict[key].append(ele)
        else:
            anagram_dict[key]=[]
            anagram_dict[key].append(ele)
    print('The size of largest subset of anagram words is:',len(max(anagram_dict.values())))
except Exception as e:
    print(e)