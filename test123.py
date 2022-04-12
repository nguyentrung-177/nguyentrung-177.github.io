def Sort(stack):
    tmpStack = []
    while len(stack) != 0:
        tmp = top(stack)
        stack.pop()
        while (len(tmpStack) != 0 and
               top(tmpStack) > tmp):
            push(stack, top(tmpStack))
            tmpStack.pop()
        push(tmpStack, tmp)
    return tmpStack


def top(stack):
    n = len(stack)
    return stack[n-1]


def push(stack, x):
    stack.append(x)


a = [-1.1, 2, 5, -6]
print(Sort(a))
