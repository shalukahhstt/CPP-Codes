import math
z = "global variable"
def example():
    x="outer function"
    def example_inner():
        y="inner function"
        # y is from the local scope,
        # x is from the enclosed scope,
        # z is from the global scope
        print(f"{x} | {y} | {z} | {math.pi}")
    # y is not accessible here since it is out of scope
    print(x)
    example_inner()
# x is not accessible here since it is out of scope
example()
print(z) # global scope
print(math.pi) # built-in scope