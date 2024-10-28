import sys


class Stack:
    def __init__(self, elements=None):
        self.stack = elements if elements else []

    def push(self, elements):
        self.stack.extend(elements)

    def pop(self, n):
        actual_popped = self.stack[-n:] if n <= len(self.stack) else self.stack[:]
        self.stack = self.stack[:-n] if n <= len(self.stack) else []
        return actual_popped[::-1]

    def length(self):
        return len(self.stack)

    def get_elements(self):
        return self.stack


input_lines = sys.stdin.read().splitlines()
input_lines += [""] * (4 - len(input_lines))

initial_length = int(input_lines[0])
initial_elements = list(map(int, input_lines[1].split())) if initial_length > 0 else []
stack = Stack(initial_elements)
total_popped = []

for operation_line in input_lines[2:4]:
    if operation_line:
        tokens = operation_line.split()
        if tokens[0] == "push":
            stack.push(map(int, tokens[1:]))
        elif tokens[0] == "pop":
            n = int(tokens[1]) if len(tokens) > 1 and tokens[1].isdigit() else 0
            total_popped += stack.pop(n)

current_length = stack.length()
if current_length > 0:
    print(f"len = {current_length}, data = {' '.join(map(str, stack.get_elements()))}")
else:
    print("len = 0")

if total_popped:
    print(f"len = {len(total_popped)}, data = {' '.join(map(str, total_popped))}")
else:
    print("len = 0")
