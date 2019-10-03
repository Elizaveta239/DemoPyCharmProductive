"""

- Supported Python Web frameworks (Django, Flask, ...)
- All features of WebStorm (Angular, React, ...)

"""
from fortytwo import App, Greeter


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
