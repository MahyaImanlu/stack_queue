# Stack project
class Stack:
    top = -1

    def __init__(self):
        self.a = []

    def push(self, value):
        self.a.append(value)
        self.top = self.top + 1

    def pop(self):
        Pop = self.a[len(self.a) - 1]
        print(f'you poped : {Pop}')
        self.a.pop()
        self.top -= 1

    def print(self):
        print(f'Stack : {self.a}')
        print(f'Top = {self.top}')


ob = Stack()
print('1 : Push\n2 : Pop\n3 : Print\n4 : Exit')
try:
    func = int(input('please enter a number of function:'))
    if func == 1:
        n = int(input('enter a number you wanna push:'))
        ob.push(n)
    elif func == 2:
        ob.pop()
    elif func == 3:
        ob.print()
    elif func == 4:
        exit()
    else:
        print('not acceptable')

    while func != 4:
        func = int(input('please enter a number of function:'))
        if func == 1:
            n = int(input('enter a number you wanna push:'))
            ob.push(n)
        elif func == 2:
            ob.pop()
        elif func == 3:
            ob.print()
        elif func == 4:
            exit()
        else:
            print('not acceptable')
except IndexError and ValueError:
    print('Your Stack is empty. You cant pop sth from your Stack')