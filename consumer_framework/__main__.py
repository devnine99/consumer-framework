import logging
import os
import sys
import importlib.util

from consumer_framework.app import ConsumerFramework
from consumer_framework.command_parser import CommandParser

logger = logging.getLogger(__name__)


def main():
    parser = CommandParser(sys.argv[1:])

    module_path = f'{os.getcwd()}/{parser.app.replace(".", "/")}.py'

    spec = importlib.util.spec_from_file_location('consumer_framework', module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    for m in mod.__dir__():
        if isinstance(getattr(mod, m), ConsumerFramework):
            sys.exit(getattr(mod, m).run())


if __name__ == '__main__':
    main()
