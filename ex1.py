import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expr):
    stack = Stack()
    expr = expr.replace('(', ' ( ').replace(')', ' ) ')
    tokens = expr.split()
    tokens.reverse()

    for token in tokens:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            if stack.is_empty():
                raise ValueError("Invalid expression")
            b = stack.pop()
            if stack.is_empty():
                raise ValueError("Invalid expression")
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.push(result)
        elif token == ')':
            # Ignoring right parenthesis, operations are immediately evaluated
            continue
        elif token == '(':
            # Ignoring left parenthesis as well
            continue

    if stack.is_empty():
        raise ValueError("Invalid expression")
    return stack.pop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)
    expr = sys.argv[1]  # Get the command line argument for the expression
    result = evaluate_expression(expr)
    print(result)
