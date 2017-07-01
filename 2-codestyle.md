# Introduction

In this section, we will quickly go through the most common code style issues that crop up.

## A. The Zen of Python

```
In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## B. Code Line Length

Generally code should be less than 80 characters per line. This is both a
legacy from the days of small monitors (historical accident), and a byproduct of desiring readability (principled design choice).

## C. Whitespace

Use four spaces, not one tab. This is because different operating systems
render tabs differently.

Don't leave training white spaces.

## D. Function, Variable and Class (or Object) Names

Pythonic code uses the following conventions:

### Function Definitions

Use lowercase names separated by underscores.

```python

# camel-cased
def myFunction():
    # do something
    return something

# pythonic
def my_function():
    # do something
    return something
```

### Variable Names

We generally use lower-case names.

```python
result = 23
```

### Object/Class Definitions

Here's the only place we use capital letters.

```python
class Shoe(object):
    def __init__(self, size):
        self.size = size

my_shoe = Shoe(10.5)
```

## E. Container operations

If you're playing with iterable items (lists, tuples, strings), consider using the `itertools` module.

## F. Looping

```python
my_nums = [1, 3, 5, 7, 9]

my_new_nums = []
for i in my_nums:
    my_new_nums.append(i+1)

my_new_nums = [i+1 for i in my_nums]

```

## G. Docstrings

These are in-code documentation for yourself.

Example:

```python
class Shoe(object):
    """
    Shoe object constructor.
    """
    def __init__(self, size):
        """
        Initialization function.

        Parameters:
        ===========
        - size (float): a floating point number that describes
                        the shoe size.
        """
        self.size = size
```
