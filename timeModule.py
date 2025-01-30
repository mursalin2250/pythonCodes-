import time


def extimecount(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        print("Total execution time:", endtime - starttime)
    return wrapper


@extimecount
def sleeptime():
    print("This is function 1")
    time.sleep(2)


sleeptime()


@extimecount
def function2():
    print("This is function 2")
    for x in range(10000000):
        pass


function2()
