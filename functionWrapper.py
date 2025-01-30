def modifiedGreet(func):
    print("Before")
    func()
    print("After")


@modifiedGreet
def greet():
    print("Hello")

@modifiedGreet
def function2():
    print("Hello again")

