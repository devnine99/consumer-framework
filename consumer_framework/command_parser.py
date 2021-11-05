import logging

logger = logging.getLogger(__name__)


class CommandParser:
    app: str

    def __init__(self, args):
        self.parse(args)

    def parse(self, args):
        try:
            self.app = args[args.index('-A')+1]
        except ValueError:
            logger.error('You have to define the app as mandatory. use \'-A\' option')
        except IndexError:
            logger.error('You have to define the app as mandatory. use \'-A\' option')
