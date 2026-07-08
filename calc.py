def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def read_file(path):
    with open(path) as f:
        return f.read()
