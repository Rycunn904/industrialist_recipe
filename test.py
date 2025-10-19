test = "Hello!"
test2 = "3"
test3 = "3.81"

print(test.isnumeric(), test)
print(test2.isnumeric(), test2)
print(test3.isnumeric(), test3)

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
print(is_integer(test), test)
print(is_integer(test2), test2)
print(is_integer(test3), test3)

print(is_float(test), test)
print(is_float(test2), test2)
print(is_float(test3), test3)