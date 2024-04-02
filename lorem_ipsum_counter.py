import os
import re
from collections import Counter

f = open("par_100.txt", "r")
# print(f.readlines())
# lines = f.readlines()
# lines.split(" ")

lst_words = list()

for line in f.readlines():
    l = line.split()
    for word in l:
        # print(word)
        word = re.sub(r'[^a-zA-Z0-9\s]', '', word)
        lst_words.append(word)
        
# print(lst_words)
word_count = Counter(lst_words)
# print(word_count)

most_freq_word = max(word_count, key=word_count.get)
print(most_freq_word) # et
print(word_count[most_freq_word]) # 159
