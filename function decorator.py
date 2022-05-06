def display(msg):
    print("entering into display function")

    print(msg)


def mid(func):
    print("entering into mid function")
    func("function is calling from mid")
    print("returning from mid function")


print("going to call mid function")
mid(display)
print("program terminated")
