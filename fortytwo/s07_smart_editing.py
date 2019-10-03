"""

- Start New Line (Shift-Enter Win/Linux/macOS)
- Use keyboard to make/extend selection (Alt Up)

- Add field to a class
- Declare type (typing in Python!)
- Introduce local variable (Alt Cmd V)
- Type Info (Ctrl Shift P)
- Automatic type checking (Try to add `name + 23`)

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/

"""

DEFAULT_NAME = "no_name"


class Customer:
    def __init__(self):
        pass

    def get_name(self):
        pass


def main():
    customer = Customer()
    name = DEFAULT_NAME
    if name != DEFAULT_NAME:
        return name
    return name


if __name__ == '__main__':
    print(main())
