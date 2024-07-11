#!/usr/bin/python3
# def square(num):
#     my_list = []
#     for n in range(1, num):
#         my_list.append(n ** 2)
#     return my_list


## List comprehension
my_list = [num **2 for num in range(1, 10)]

print(my_list)

## Generator expressions uses a brack() instead 

gen_list = (num **2 for num in range(1, 10))
print(gen_list)

## Convert the generator to a list 

print(list(gen_list))

## Generator expressions allow us to create an iterator in a single line of code

## Loop 

for num in (num ** 2 for num in range(1,10)):
    print(num)
