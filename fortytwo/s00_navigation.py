"""

Simple navigation
- Find Action (Cmd Shift A)

Navigate to File (Shift-Ctrl-N Win/Linux, Shift-Cmd-O macOS)
- Look for ``02``
- Look for `fo/mo` to get ``fortytwo/models.py``
- Look for ``poolm`` to look in dependencies

Navigate to Symbol (Shift-Ctrl-Alt-N Win/Linux, Alt-Cmd-O macOS)
- `greet` - shows functions, classes, files
- Also goes into dependencies, e.g. `SerReg` for `wired.ServiceRegistry`

Go To Definition
- Cmd-B on `App`, then `ServiceRegistry`
- Use left/right brackets to return/descend

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/

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
