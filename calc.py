def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def subtract(x,y):
    return x - y

if __name__ == "__main__":
    x = input("first number = ")
    y = input("second number = ")
    operation = input("1.add/2.subtract/3.multiply/4.divide: ")
    if operation == 1:
        result = add(x,y)
    elif operation == 2:
        result = subtract(x,y)
    elif operation == 4:
        result = divide(x,y)
    elif operation == 3:
        result = multiply(x,y)
    else:
        print("Unrecognized input")
    print("result is: " + str(result))
