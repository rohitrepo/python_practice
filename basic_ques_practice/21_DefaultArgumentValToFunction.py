#passing default arguments to a function if no value is passed during invocation

def printFunc (str = "Hello World", times = 5):
    for i in range (times):
        print(str)

#here it will take default arguments
printFunc()

#here it will take arguments you have passed
printFunc("Rohit", 4)