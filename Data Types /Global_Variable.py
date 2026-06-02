# def myfunc():
#     global x
#     x = "Vinay kumar"
# myfunc()
# print("Python developer is " + x)
x="2" #this is a global variable
def myfunc():
    #local scope
    x = "Vinay kumar" #inside function x is local variable
    print("Python developer is " + x)
myfunc()
print("Python developer is " + x)