"""

View Parameter Info

Quickly see function arguments and argument types. (F1)
- ``choices`` is weird, what does it want?

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/

"""

from random import choices

from fortytwo import App
from fortytwo.models import Greeter

customers = ('Larry', 'Alice', 'Sam')


def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        customer = choices()  # Not sure the parameters here
        greeting = greeter(customer)
        return greeting


if __name__ == '__main__':
    print(main())
