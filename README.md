# Introduction to Pathon Generator

Generators are functions that hold their own state but it is too small for a class.
Generators also have their own iterators.

Have you ever had to work with a dataset so large that it overwhelmed your machine's memory?
Or maybe you have a complex function that needs to maintain an internal state every time it's 
called, but the function is too small to justify creating its own class. In these cases and 
more, generators and the Python `yield` statement are here to help.




### Concerns:

[-] Mental Models and technical communication on how **generators** work under the hood. 
[-] How to create **generator functions and expressions**
[-] How the **Python yield** statement works
[-] How to use multiple Python Yield statements in a generator function
[-] How to use **advanced generator methods**
[-] How to build data pipelines with multiple generators


## Generator Functions 

They are written like regular function except that they have the `yield` key word.

The `yield` key word then returns a lazy iterator(which means that the content are not stored in memory).


Inorder to see what is inside a generator object, you have to convert it into a data structure 
like ist `list(generator_object)`.

generator object can also be looped through with the `next()` method. 

generator object can get exhaused (that is used up) when it is converted.

data stored in memory in functions can be stored in memory, but generators get 
exhausted when used.


Generators are a powerful tool in Python for  managing memory efficiently, especially when dealing with large datasetss or streams of data. Here's how they help with memory:

## 1. Lazy Evaluation

Generators uses lazy evaluation, which means they produce items one at a time and only when requested. This contrast with lists, which compute and store all items  in memory at once. 
By generating items on-the-fly, generators can handle large data sets without requiring the memory to store all elments simultaneously.

**Code samples**

```py
def generate_numbers(n):
    for i in range(n):
        yield i

gen = generate_numbers(1000000)

# This won't consume much memory because values are generated one at a time
for number in gen:
    print(number)

```


## 2. Reduced Memory Footprint

Since generators do not store their items in memory, they have a smaller memory footprint. This is particularly useful when processing large files or data streams, such as reading lines from a large file.


```py
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

# This will read lines one by one without loading the entire file into memory
for line in read_large_file('large_file.txt'):
    process_line(line)
```

## 3. Efficient Data Pipelines

Generators can be chained together to form data processing pipelines. Each generator in the chain processes and yields data to the next, maintaining low memory usage throughout.

```py
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines):
    for line in lines:
        if 'error' in line:
            yield line

def process_lines(lines):
    for line in lines:
        print(f"Processing: {line}")

# Creating a pipeline
lines = read_large_file('large_log_file.txt')
filtered_lines = filter_lines(lines)
process_lines(filtered_lines)
```

## 4. Infinite Sequences

Generators can represent infinite sequences, which are impossible to store in memory. This is useful for applications needing continuous data streams.

```py
def infinite_sequence(start=0):
    while True:
        yield start
        start += 1

gen = infinite_sequence()

# This can run indefinitely, producing values one at a time
for number in gen:
    print(number)
    if number >= 10:  # Stop the loop after a few iterations for demonstration
        break

```



## Summary

Generators are an efficient way to handle large data sets, process streams of data, and manage memory usage. They produce items one at a time, on-the-fly, without the need to store all elements in memory, making them ideal for scenarios where memory efficiency is critical.
