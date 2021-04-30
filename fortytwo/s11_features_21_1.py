"""

Most interesting features of 2021.1 release:
https://www.jetbrains.com/pycharm/whatsnew/

1. Code With Me
- New collaborative editing tool

2. Auto-import for modules
type `subprocess.Popen` -> adds `import subprocess`
The same for pd.DataFrame

3. Completion for multiple arguments
f(a, -> f(a, b, c, d)

4. Tool window for Python packages

"""

from fortytwo import App, Greeter


def do_calculations(a, b, c, d):
    return a + b + c + d


def read_values():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))
    return do_calculations()


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter('Larry')
        return greeting


if __name__ == '__main__':
    print(main())
