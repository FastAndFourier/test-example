def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def test_add(a, b):
    assert add(2,3) == 5

def test_subtract(a, b):
    assert substract(2,3) == -1
    
def test_multiply(a, b):
    assert multiply(2, -1) == 2
