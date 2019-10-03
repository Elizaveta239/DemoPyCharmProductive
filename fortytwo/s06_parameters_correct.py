"""

A dummy file to run tests

"""
from fortytwo import App, Greeter


def foo(a):
    b = 2
    return a + b


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
