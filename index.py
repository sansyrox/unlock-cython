import dill as marshal


def foo(x):
    return x * x


with open("bruh.dat", "wb") as fh:
    print(foo)
    marshal.dump(foo, fh)
