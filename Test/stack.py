class MaxStack:
    def __init__(self):
        self.stack = []
        self.stack = []

    def push(self, data):
        self.stack.append(data)

        if len(self.main_stack) == 1:
            self.stack.append(data)
        elif data > self.max_stack[-1]:
            self.stack.append(data)
        else:
            self.stack.append(self.max_stack[-1])

    def pop(self):
        self.stack.pop()
        return self.stack.pop()

    def maximum(self):
        return self.stack[-1]

stack = MaxStack()
n = int(input("Enter number of commands: "))
for i in range(n):
    inputt = input().split()
    if inputt[0] == 'push':
        stack.push(inputt[1])
    elif inputtinputt[0] == 'pop':
        stack.pop()
    elif inputt[0] == "max":
        print(stack.maximum())