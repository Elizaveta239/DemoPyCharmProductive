"""

Reformat Code

Tell PyCharm to clean up indentation and other code style in your file.
- 3 warnings below
- Reformat File (``Ctrl-Alt-Shift-L`` Win/Linux, ``Alt-Cmd-L`` macOS)
- Reformat Code (`Ctl-Alt-L`)

Analyze the whole project:
- Inspect code

Repo: https://github.com/pauleveritt/42-workshop
Playlist: https://www.jetbrains.com/pycharm/guide/playlists/42/

"""

from fortytwo import App, Greeter
def main():
    site = App()
    with site as container:
        greeter = container.get(Greeter)
        greeting = greeter(     'Larry')
        return greeting


if __name__ == '__main__':
 print(main())
