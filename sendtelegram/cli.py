import sys

import argh

from .commands import send_message


def main():
    parser = argh.ArghParser()
    parser.set_default_command(send_message)
    parser.dispatch()


if __name__ == "__main__":
    sys.exit(main())
