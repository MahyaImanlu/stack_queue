# Queue project
class Queue:
    front = -1
    rear = -1

    def __init__(self):
        self.a = []

    def enqueue(self, value):
        self.a.append(value)
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

    def dequeue(self):
        print(f'dequeue:{self.a[0]}')
        self.a.pop(0)

        if len(self.a) == 0:
            self.rear = -1
            self.front = -1

        else:
            self.front += 1
            self.rear = self.rear

    def print(self):
        print(f'Queue : {self.a}')
        print(f'front : {self.front}')
        print(f'rear : {self.rear}')


ob = Queue()

print('1 : Enqueue\n2 : Dequeue\n3 : print\n4 : exit')

try:
    func = int(input('please enter a number of function:'))
    if func == 1:
        n = int(input('enter a number you wanna enqueue:'))
        ob.enqueue(n)
    elif func == 2:
        ob.dequeue()
    elif func == 3:
        ob.print()
    elif func == 4:
        exit()
    else:
        print('Not acceptable. This function is not available')

    while func != 4:
        func = int(input('please enter a number of function:'))
        if func == 1:
            a = int(input('enter a number you wanna enqueue:'))
            ob.enqueue(a)
        elif func == 2:
            ob.dequeue()
        elif func == 3:
            ob.print()
        elif func == 4:
            exit()
        else:
            print('Not acceptable. This function is not available')

except IndexError and ValueError:
    print('Your Queue is empty. You cant pop sth from your Queue')
