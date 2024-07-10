#!/usr/bin/python3
some_words = ["potatoes", "shallow", "voice", 
"conversation", "more", "myself", "thirty", "certainly"]

def contains_i(words):
    i_words = []
    for word in words:
        if "i" in word:
            i_words.append(word)
    return i_words


print(contains_i(some_words))

