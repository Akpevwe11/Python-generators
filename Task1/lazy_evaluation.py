#!/usr/bin/python3
def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(1000000)

# This won't consume much memory because values are generated one at a time
for number in gen:
    print(number)
