#!/usr/bin/python3
some_words = ["potatoes", "shallow", "voice", 
"conversation", "more", "myself", "thirty", "certainly"]

def contains_i(words):
    for word in words:
        if "i" in word:

            yield word
    


print(contains_i(some_words))

### to see what is inside the generator object 
print(list(contains_i(some_words)))

### Because generators get exhaused when used up, so I need to call it anytime i need it
### yielded value from a generator does not get stored in memory

gen_ob = contains_i(some_words)

while True:
    try:
        word = next(gen_ob)
        print(word)
    except StopIteration:
        break

#print(next(gen_ob))
#print(next(gen_ob))
#print(next(gen_ob))
#print(next(gen_ob))



