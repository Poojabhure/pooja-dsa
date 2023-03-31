#!/usr/bin/env python
# coding: utf-8

# In[22]:


get_ipython().set_next_input('Q.1 Write a program to find all pairs of an integer array whose sum is equal to a given number');get_ipython().run_line_magic('pinfo', 'number')

def find_pairs(arr, target_sum):
    pairs = []
    # loop through the array and check each element
    for i in range(len(arr)):
        # loop through the rest of the array and check each element
        for j in range(i+1, len(arr)):
            # check if the sum of current pair is equal to the target sum
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    # return the list of pairs
    return pairs

# Example usage
arr = [1, 2, 3, 4, 5]
target_sum = 6
pairs = find_pairs(arr, target_sum)
print(pairs)


EXAMPLE:array = [1, 2, 3, 4, 5]
        target_sum = 7
        pairs  = find_pairs(array, target_sum)
        print (pairs)
        Output: [ [2, 5],[3, 4] ]


# In[24]:


Q.2  Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(arr):
    # initialize two pointers, one at the beginning and one at the end of the array
    start = 0
    end = len(arr) - 1
    
    # loop through the array and swap the elements at the start and end pointers
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)

EXAMPLE:  array = [1, 2, 3, 4, 5]
          reverse_array=[5, 4, 3, 2, 1]	





# In[ ]:


get_ipython().set_next_input('Q.3   Write a program to check if two strings are a rotation of each other');get_ipython().run_line_magic('pinfo', 'other')


# In[9]:


def are_rotations(str1, str2):
    # check if the length of both strings is the same
    if len(str1) != len(str2):
        return False
    
    # concatenate the first string to itself
    temp = str1 + str1
    
    # check if the second string is a substring of the concatenated string
    if str2 in temp:
        return True
    else:
        return False

# Example usage
str1 = "abcd"
str2 = "cdab"
if are_rotations(str1, str2):
    print("The strings are rotations of each other.")
else:
    print("The strings are not rotations of each other.")
    
    
    ex: 
        rotations("hello", "lohel") = True
        rotations("world", "ldwor") = True
        rotations("hello", "lloeh") = False


# In[10]:


get_ipython().set_next_input('Q.4  Write a program to print the first non-repeated character from a string');get_ipython().run_line_magic('pinfo', 'string')

    def first_non_repeated_char(string):
    # create a dictionary to store the count of each character
    char_count = {}
    
    # loop through the string and update the count of each character in the dictionary
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # loop through the string again and return the first character with a count of 1
    for char in string:
        if char_count[char] == 1:
            return char
    
    # if there are no non-repeated characters, return None
    return None

# Example usage
string = "hello world"
result = first_non_repeated_char(string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("There are no non-repeated characters in the string.")

 

 EXAMPLE:
    
    first_non_repeated_char("hello")
    'h'
    first_non_repeated_char("aabbc")
    'c'
    first_non_repeated_char("aabbcc")
    None


# In[11]:


Q.5 Read about the Tower of Hanoi algorithm. Write a program to implement it.


EXAMPLE:
    >>> tower_of_hanoi (3, 'A', 'C', 'B')
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C


ef tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    tower_of_hanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')


# In[12]:


Q.6  Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

   def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for token in postfix:
        if token not in operators:
            # If the current token is an operand, push it onto the stack
            stack.append(token)
        else:
            # If the current token is an operator, pop the top two operands from the stack and
            # concatenate them with the operator in prefix notation. Push the resulting string
            # back onto the stack.
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = token + operand2 + operand1
            stack.append(expression)

    # The final result is the prefix expression, which is the top element of the stack.
    return stack[-1]

# Example usage
postfix = "34+5*"
prefix = postfix_to_prefix(postfix)
print("Prefix expression:", prefix)



EXAMPLE:
    >>> postfix_to_prefix('2 3 + 4 *')='* + 2 3 4'




# In[14]:


Q.7  Write a program to convert prefix expression to infix expression.

     def prefix_to_infix(prefix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for token in reversed(prefix):
        if token not in operators:
            # If the current token is an operand, push it onto the stack
            stack.append(token)
        else:
            # If the current token is an operator, pop the top two operands from the stack and
            # concatenate them with the operator in infix notation. Enclose the resulting string
            # in parentheses and push it back onto the stack.
            operand1 = stack.pop()
            operand2 = stack.pop()
            expression = '(' + operand1 + token + operand2 + ')'
            stack.append(expression)

    # The final result is the infix expression, which is the top element of the stack.
    return stack[-1]

# Example usage
prefix = "*+345"
infix = prefix_to_infix(prefix)
print("Infix expression:", infix)




EXAMPLE:
    >>> prefix_to_infix('* + 2 3 4')='(2 + 3) * 4'


# In[16]:


Q.8  Write a program to check if all the brackets are closed in a given code snippet.

  def check_brackets(code):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in code:
        if char in bracket_pairs.values():
            # If the current character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_pairs.keys():
            # If the current character is a closing bracket, pop the top element from the stack
            # and compare it to the current closing bracket.
            if not stack or bracket_pairs[char] != stack.pop():
                return False

    # If the loop completes and the stack is empty, return True as all the brackets are closed.
    # If the stack is not empty, return False as some brackets are not closed.
    return not stack

# Example usage
code1 = "(2 + 3) * {5 - 4}"
code2 = "print('Hello, World!'"
code3 = "while (True) {"
print("Code 1 brackets are balanced:", check_brackets(code1))
print("Code 2 brackets are balanced:", check_brackets(code2))
print("Code 3 brackets are balanced:", check_brackets(code3))




EXAMPLE:
       >>> check_brackets('(a + b) * [c - {d / e}]') = True
       >>> check_brackets('print("Hello, world!"') = False


# In[17]:


Q.9 Write a program to reverse a stack.

class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def _len_(self):
        return self.size()

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    temp_stack = Stack()

    # Pop each element from the original stack and push it onto temp_stack
    while not stack.is_empty():
        temp_stack.push(stack.pop())

    # Pop each element from temp_stack and push it back onto the original stack
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

# Example usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Original stack:", [item for item in s.items])
reverse_stack(s)
print("Reversed stack:", [item for item in s.items])



EXAMPLE:
    >>> stack = [1, 2, 3, 4, 5]
    >>> reverse_stack =  [5, 4, 3, 2, 1]



# In[19]:


Q.10   Write a program to find the smallest number using a stack.
   class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def _len_(self):
        return self.size()

    def size(self):
        return len(self.items)

def find_smallest_number(stack):
    min_stack = Stack()

    # Push the first element onto both stacks
    min_stack.push(stack.peek())
    stack.pop()

    # Iterate over the remaining elements
    while not stack.is_empty():
        # Compare the new element with the current minimum
        if stack.peek() < min_stack.peek():
            min_stack.push(stack.peek())
        else:
            min_stack.push(min_stack.peek())

        stack.pop()

    # The top element of min_stack is the smallest number
    return min_stack.peek()

# Example usage
s = Stack()
s.push(5)
s.push(2)
s.push(7)
s.push(1)
s.push(8)

print("Stack:", [item for item in s.items])
print("Smallest number:", find_smallest_number(s))




EXAMPLE:
    >>> stack = MinStack()
>>> stack.push(5)
>>> stack.push(2)
>>> stack.push(7)
>>> stack.push(1)
>>> print(stack.get_min())
1
>>> stack.pop()
1
>>> stack.pop()
7
>>> print(stack.get_min())
2




# In[ ]:




