from stack import Stack

def inverse(string):
    stack = Stack()
    inv = ""
    for i in string:
        stack.push(i)
    while not stack.is_empty():
        inv += stack.pop()
    return inv


print(inverse(str))
