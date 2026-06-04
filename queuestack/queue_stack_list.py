#queue_stack _list

queue = [1,2,3]

def enqueue(element):
    queue.append(element)


def peek():
    return queue[0]

def dequeue():
    dequeue_element = peek()
    queue.remove(dequeue_element)
    return queue

def size():
    return len(queue)

def is_empty():
    return len(queue) == 0


def main():
    print(queue)
    enqueue(4)
    print(queue)
    print(peek())
    dequeue()
    print(queue)
    print(size())
    print(is_empty())
    print(stack)
    push(4)
    peek_stack()
    pop()
    size_stack()
    isempty_stack()

stack = []

def push(element):
    stack.append(element)
    return print(stack)

def pop():
    stack.pop(-1)
    return print(stack)
    

def peek_stack():
    return print(queue[-1])

def isempty_stack():
    if len(stack) == 0:
        return print(True)
    else:
        return print(False)

def size_stack():
    return print (len(stack))

push(5)



if __name__ == "__main__":
    main()