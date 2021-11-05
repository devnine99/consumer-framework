import sys
import importlib.util

from consumer_framework.app import Consumer


def main():
    args = sys.argv[1:]
    try:
        app_index = args.index('-A')
        app = args[app_index+1]
    except (ValueError, IndexError):
        print('앱이 지정되지 않았습니다.')
        return

    module_name = 'consumer_framework'
    module_path = sys.argv[0].replace('consumer', f'{app.replace(".", "/")}.py')

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for m in mod.__dir__():
        if isinstance(getattr(mod, m), Consumer):
            sys.exit(getattr(mod, m).run())
