"""

VCS support

- Review changes in commit message
- Reword commit message
- Undo commit
- Partial commit

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
