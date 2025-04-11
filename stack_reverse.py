class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def push(self, n_value):
        self.items.append(n_value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last= self.size() - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack= Stack()
print(stack.is_empty())
if stack.is_empty():
    print("stack is empty")

greet = "あさださあ"#"Good Morning Sun!"
print(greet)

for c in greet:
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()

print(">>reverse!!>>",reverse)
