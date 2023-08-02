import sys
import os
from time import sleep

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
TIME_TICKER_INTERVAL_SECONDS = 1

OPTIONS = {
    's': "SHUT DOWN",
    'r': "RESTART",
    'h': "HIBERNATE",
    'l': "LOG OFF",
    'z': "SLEEP"
}

def countdown(opt, behav, mins) -> None:
    try:
        if opt == 'z':
            import keyboard as kb
    except ModuleNotFoundError:
        print("The sleep option requires the 'keyboard' module, but was not found.\nUse command 'pip3 install keyboard' to install module.\n")
        sys.exit()

    mins_left = mins
    secs_left = 0
    
    print(f"{behav} IN {mins} MINUTES countdown started. Press Ctrl-C to Cancel.")
    print(f"Time remaining: {mins_left}:{secs_left:02d}")
    sleep(TIME_TICKER_INTERVAL_SECONDS)
    mins_left -= 1

    while mins_left >= 0:
        secs_left = 60 - TIME_TICKER_INTERVAL_SECONDS

        while secs_left >= 0:
            print(LINE_UP, end=LINE_CLEAR)
            print(f"Time remaining: {mins_left}:{secs_left:02d}")
            secs_left -= TIME_TICKER_INTERVAL_SECONDS
            sleep(TIME_TICKER_INTERVAL_SECONDS)

        mins_left -= 1
    
    print(f"=={behav}==")

    if opt == 'z':
        kb.send("win+x")
        sleep(1)
        kb.send("u")
        sleep(1)
        kb.send("s")
    else:
        os.system(f"shutdown /{opt}")

def main() -> int:
    try:
        opt_arg = sys.argv[1]
        behav_text = OPTIONS[opt_arg]

        try:
            mins_arg = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        except (IndexError, ValueError):
            print("Invalid time argument. Must be a positive integer of minutes.")
        else:
            countdown(opt_arg, behav_text, mins_arg)
    except KeyboardInterrupt:
        print("==Aborted==")
    except (IndexError, KeyError):
        print("No or invalid behaviour argument. Accepted arguments:\n" \
              " s : shutdown\n" \
              " r : restart\n" \
              " h : hibernate\n" \
              " l : log off\n" \
              " z : sleep (requires 'keyboard' module)\n")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
