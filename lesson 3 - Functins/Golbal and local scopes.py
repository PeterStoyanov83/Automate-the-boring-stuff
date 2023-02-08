spam = "hello"  # Global variable

def eggs():
    global spam # Global variable
    spam = 42  # local variable with assigned variable it is acting on the global scope variable
    
    print(spam)

eggs()

print(spam)