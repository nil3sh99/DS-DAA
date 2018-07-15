from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Appended item is: " + item)

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize -1)

    return stack.pop()

# Driver program to test the above functions

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
# add your insertions here the same way as above
print("Before popping up the value : " + str(stack))
# pop the values multiple times using the same syntax as above
print(pop(stack) + " popped from stack")
print("After popping up the stack looks : " + str(stack))
print("Top item is " + str(stack[-1:]))
#print(createStack())