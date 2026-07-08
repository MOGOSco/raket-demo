def divide(a,b):
    return a/b  # still no guard

def risky(x):
    return open(x).read()  # unclosed file handle
