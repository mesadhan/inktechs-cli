#!/usr/bin/python
import sys

from inktechs.process_action import ProcessAction


def main():
    print('Hello! from inktechs cli')
    args = sys.argv[1:]

    process_action = ProcessAction()
    process_action.process_typical_arguments(args)


if __name__ == '__main__':
    main()
