# offtimer.py

A Python command-line utility for Windows that lets you countdown to a shut down, restart, hibernate, log off or sleep[^1].
[^1]: The sleep option uses the Win+X menu found on Windows 10 and 11, and the 'keyboard' python module.

### Usage

In the command line (inside the file's directory), type:
`python .\offtimer.py <behaviour> <minutes>`

Behaviour argument must be specified (there is no default):
| Argument | Action to be taken |
| :---: | --- |
| `s`| Shut down |
| `r` | Restart |
| `h` | Hibernate |
| `l` | Log off |
| `z` | Sleep (requires 'keyboard' module) |

If no time argument is provided, the action will be taken immediately.
Press <kbd>Ctrl</kbd>+<kbd>C</kbd> to abort before the timer runs down.

### Example

To hibernate in 25 minutes, type `python .\offtimer.py h 25`.
The utility will show a countdown of the time remaining, then execute the behaviour specified.

![Utility counting down to hibernate inside Windows Terminal](example_image.png)
