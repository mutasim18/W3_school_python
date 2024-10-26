# Variables that are created outside of a function are known as global variables.
x = 'bro'
def myfunc():
    print("Whats up" + " " + x)
myfunc()

"""
If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was,
global and with the original value.
"""
x = 'bro'
def myfunc():
    x = "homie"
    print("Whats up" + " " + x)
myfunc()
print("Whats up" + " " + x)

"""
Normally, when you create a variable inside a function, that variable is local,
 and can only be used inside that function.

To create a global variable inside a function,
 you can use the global keyword.
"""
def myfunc():
    global x
    x = "bro"
myfunc()
print("YO " + x)

"""
To change the value of a global variable inside a function, 
refer to the variable by using the global keyword:
"""
x = "cat"
def myfunc():
    global x
    x = "geez"
myfunc()
print("YO " + x)