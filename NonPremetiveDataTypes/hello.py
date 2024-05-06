def word_spelled(words, letters):
    single_word_counter={}
    for letter in letters:
        if letter in single_word_counter:
            single_word_counter[letter]+=1
        else:
            single_word_counter[letter]=1
    print(single_word_counter)
    for word in words:
        can_spelled = True
        for single_char in word.lower():
            if single_char in single_word_counter and word.lower().count(single_char)<=single_word_counter[single_char]:
                continue
            else:
                can_spelled =False
                break
        if can_spelled:
            print(f'{word} can spelled')
        else:
            print(f'{word} can not spelled')


words = ["Acura", "Ford", "Ferrari", "Honda", "Nissan", "Datsun"]
letters = ["a", "f", "r", "r", "e", "i", "o", "h", "c", "s", "u", "w", "a", "n", "d"]

word_spelled(words, letters)


