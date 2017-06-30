# variable names

Generally speaking, give your variables names that make sense.

# conditionals

Newcomers to Python would oftentimes write something like the following:

```python
if cond == True:
    # do something
else:
    # do another thing
```

However, the Pythonic way to handle it is as such:

```python
if cond:
    # do something
else:
    # do another thing
```

Doing so omits unnecessary text.

Sometimes, we also check whether the value of a variable is `None`. Newcomers to Python may write it this way:

```python
if value == None:
    # do something
```

However, Pythonic code would be written as such instead:

```python
if value is None:
    # do something
```

# making a list of numbers

Let's say I want to make a list of integers from 0 to 13, inclusive. There are a few ways to do it.

(1) `for` loops

```python
integers = []
for i in range(14):
  integers.append(i)
```

(2) list comprehensions
```python
integers = [i for i in range(13)]
```

(3) casting range as lists
```python
integers = list(range(13))
```

Which do we choose?

Generally speaking, the community has converged on **list comprehensions** as being considered "the most Pythonic". Recommended to go with that where possible.

# refactoring code

If you find yourself copy/pasting code, even just once, it is a sign that you have to refactor your code. Here's an example to illustrate the point.

```python
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head):
        self.head = head

    def insert(node, N):
        """
        Inserts a node into the DoublyLinkedList such that it is now the node
        at position N.
        """
        i = 0          # note how these next few lines are repeated in the
        n = self.head  # `delete` function.
        while i < N:
            n = n.next
            i += 1
        node.next = n.next
        n.prev.next = node

    def delete(N):
        i = 0
        n = self.head
        while i < N:
            n = n.next
            i += 1
```

We could have refactored the code into a `get(self, N)` function.

# `__repr__`

If you create an object class, `__repr__(self)` is a very useful object method to have.
