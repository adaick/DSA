class MaxStack:
    def __init__(self):
        self.stackmain = []
        self.stackmax = []

    def push(self, data):
        self.stackmain.append(data)

        if len(self.stackmain) == 1:
            self.stackmax.append(data)
        elif data > self.stackmax[-1]:
            self.stackmax.append(data)
        else:
            self.stackmax.append(self.stackmax[-1])

    def pop(self):
        self.stackmax.pop()
        return self.stackmain.pop()

    def maximum(self):
        return self.stackmax[-1]

stack = MaxStack()
n = int(input("Enter number of commands: "))
for i in range(n):
    inputt = input().split()
    if inputt[0] == 'push':
        stack.push(inputt[1])
    elif inputt[0] == 'pop':
        stack.pop()
    elif inputt[0] == "max":
        print(stack.maximum())