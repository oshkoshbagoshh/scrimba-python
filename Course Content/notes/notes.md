## Notees



![alt text](image.png)

---
In Python, a tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but they have some key differences:

1. Immutability: Once a tuple is created, its elements cannot be changed. You cannot add, remove, or modify elements in a tuple.

2. Syntax: Tuples are defined using parentheses `()`, although the parentheses are optional in some cases. Elements in a tuple are separated by commas.

Here are some examples of creating and using tuples in Python:

1. Creating a tuple:
```python
my_tuple = (1, 2, 3)
another_tuple = 4, 5, 6  # Parentheses are optional
empty_tuple = ()
single_element_tuple = (7,)  # Note the trailing comma
```

2. Accessing elements in a tuple:
```python
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1
print(my_tuple[1:])  # Output: (2, 3)
```

3. Attempting to modify a tuple (raises an error):
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 4  # Raises a TypeError: 'tuple' object does not support item assignment
```

4. Tuple unpacking:
```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

5. Tuple methods:
```python
my_tuple = (1, 2, 3, 2, 4)
print(my_tuple.count(2))  # Output: 2
print(my_tuple.index(3))  # Output: 2
```

6. Iterating over a tuple:
```python
my_tuple = (1, 2, 3)
for item in my_tuple:
    print(item)
```

Tuples are commonly used in situations where you want to store a collection of related values that should not be modified. They are faster than lists and can be used as keys in dictionaries or as elements in sets.

Some common use cases for tuples include:
- Returning multiple values from a function
- Representing a fixed set of values, such as coordinates or database records
- Passing immutable arguments to functions

Tuples provide a way to create immutable sequences of elements in Python, ensuring that the data remains unchanged throughout the program's execution.

---

- Sets are unordered, and there can be no duplicates in them

Python provides three built-in types for storing collections of data: lists, tuples, and sets. Each has its own characteristics and use cases:

### Lists
- **Mutable:** You can change, add, or remove elements.
- **Ordered:** The elements have a defined order, and that order will not change.
- **Syntax:** Created using square brackets `[]`.
- **Duplicates Allowed:** Lists can contain duplicate elements.
- **Example Usage:** When you need a collection that can change over time, and order matters.

```python
my_list = [1, 2, 3, 3]
my_list.append(4)  # Adding an element
print(my_list)  # Output: [1, 2, 3, 3, 4]
```

### Tuples
- **Immutable:** Once created, you cannot change, add, or remove elements.
- **Ordered:** The elements have a defined order.
- **Syntax:** Created using parentheses `()`, but can also be defined without them.
- **Duplicates Allowed:** Tuples can contain duplicate elements.
- **Example Usage:** When you need an ordered collection of items that should not change through the program.

```python
my_tuple = (1, 2, 3, 3)
# my_tuple.append(4) would raise an AttributeError
print(my_tuple)  # Output: (1, 2, 3, 3)
```

### Sets
- **Mutable:** You can add or remove elements, but you cannot change existing elements.
- **Unordered:** The elements do not have a defined order, and their order can change.
- **Syntax:** Created using curly braces `{}` or the `set()` function for an empty set.
- **Duplicates Not Allowed:** Sets automatically remove duplicate elements.
- **Example Usage:** When you need to ensure all elements are unique or to perform set operations like union, intersection.

```python
my_set = {1, 2, 3, 3}
my_set.add(4)  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4} because duplicates are not allowed
```

### Choosing Between Them
- Use **lists** when you need an ordered collection that you might need to alter.
- Use **tuples** for ordered collections of items that should not change.
- Use **sets** when you need uniqueness for the elements and don't care about the order.



---


# while condition:
#     code
#     iterator
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> 
#3. How long should we repeat?
#  -> 

    
    
---
## Enumerate 
- used to add numbers to a list 
- syntax:
  ```python
  for num, letter in enumrate('python',start=5):
    print(num,letter)

    ```
Output:
![alt text](image-1.png)

---
## Sort() and Sorted()


## Dictionaries



![alt text](image-2.png)


## Filehandling - Reading Files

File handling in Python is a critical skill for reading from and writing to files on your computer. Python provides built-in functions for opening, reading, writing, and closing files. Here's a basic guide to file handling operations:

### Opening a File
Use the `open()` function to open a file. The syntax is:
```python
file_object = open(file_name, access_mode)
```
- `file_name` is the name of the file to be opened.
- `access_mode` determines the mode in which the file has to be opened, e.g., read, write, append, etc. Common modes include:
  - `'r'` for reading (default),
  - `'w'` for writing (creates a new file or truncates the existing file),
  - `'a'` for appending,
  - `'b'` for binary mode,
  - `'+'` for read/write mode.

### Reading from a File
- **Read the entire file**: Use `file_object.read()`.
- **Read one line at a time**: Use `file_object.readline()`.
- **Read all lines as a list**: Use `file_object.readlines()`.

Example:
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Writing to a File
- **Write a string**: Use `file_object.write(string)`.
- **Write multiple strings**: Use `file_object.writelines(list_of_strings)`.

Example:
```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
```

### Appending to a File
Similar to writing, but opens the file in append mode `'a'` so that new data will be added at the end of the file.
```python
with open('example.txt', 'a') as file:
    file.write("\nAppending a new line.")
```

### Closing a File
It's crucial to close a file after your operations are done to free up system resources. The `with` statement automatically handles this.
```python
with open('example.txt', 'r') as file:
    content = file.read()
# No need to explicitly call file.close() here
```

### The `with` Statement
The `with` statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers. For file operations, it ensures that the file is properly closed after its suite finishes, even if an exception is raised on the way.

This basic overview covers fundamental file handling operations in Python. Depending on your specific needs, you might explore more advanced topics like working with files in binary mode or handling large files in chunks.

## Exceptions: Try/Except, Raise
In Python, the `try` and `except` blocks are used for exception handling, allowing you to catch and handle errors or exceptions that occur during the execution of a block of code. Here's how they work:

- **`try` block**: You wrap the code that might throw an exception in a `try` block.
- **`except` block**: If an exception occurs in the `try` block, the flow of control is passed to an `except` block, allowing you to handle the error.

Here's a simple example to illustrate their use:

```python
try:
    # Code block where you suspect an error may occur
    result = 10 / 0
except ZeroDivisionError:
    # Handling a specific exception
    print("You can't divide by zero!")
except Exception as e:
    # Handling any other exceptions
    print(f"An error occurred: {e}")
else:
    # This block is executed if no exceptions are raised
    print("Operation successful.")
finally:
    # This block is executed no matter what, and is often used for cleanup
    print("Execution completed.")
```

In this example:
- The `try` block contains code that will raise a `ZeroDivisionError`.
- The first `except` block catches and handles the `ZeroDivisionError`, printing a message to the user.
- The second `except` block is a generic catch-all for any other exceptions that might occur. It captures the exception as `e` and prints a message.
- The `else` block would run only if no exceptions are caught. Since an exception is raised in the `try` block, the `else` block is skipped.
- The `finally` block runs regardless of whether an exception was caught or not, making it useful for cleanup activities, such as closing files or releasing resources.

## Classes and Objects
- Classes are blueprints
- Objects are the actual things you built
- variables are attributes
- functions are methods


## Inheritance

## Modules 

## Zip / Unzip

## Lambda Functions 

## Comprehensions - Lists 

## Comprehensions - Dictionary 

## Randomness

## Timeit and performance

## Project - Crypto Machine

## Project - Math Tutor

## Project - Marble / Trading Game 

## Bonus: Project - Palindromes 
