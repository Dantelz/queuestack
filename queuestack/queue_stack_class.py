class Stack:
    def __init__(self, stack):
        self.stack = stack

def push(self, element):
    self.stack.append(element)
    return self.stack

def pop(self):
    self.stack.pop()
    return self.stack

def peek(self):
    return self.stack[-1]

def isempty(self):
    return len(self.stack) == 0

def size(self):
    return len(self.stack)


class Queue:
    def __init__(self, stack):
        self.stack = stack

def enqueue(self, element):
    self.stack.append(element)
    return self.stack

def dequeue(self):
    self.stack.pop()
    return self.stack

def peekqueue(self):
    return self.stack[0]

def isemptyqueue(self):
    return len(self.stack) == 0

def sizequeue(self):
    return len(self.stack)


def main():
    print("stack")
    c2 = Stack([1, 2, 3])
    print(c2.push(4))
    print(c2.peek())
    print(c2.pop())
    print(c2.isempty())
    print(c2.size())
    print("queue")
    c1 = Queue([1, 2, 3])
    print(c1.enqueue(4))
    print(c1.peekqueue())
    print(c1.dequeue())
    print(c1.isemptyqueue())
    print(c1.sizequeue())

main()