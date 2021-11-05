import sys
import importlib.util

from consumer_framework.command_parser import CommandParser


def main():
    parser = CommandParser(sys.argv[1:])
    module_name, app_name = parser.app.split(':')
    mod = importlib.import_module(module_name)
    app = getattr(mod, app_name)
    sys.exit(app.run())


if __name__ == '__main__':
    main()
