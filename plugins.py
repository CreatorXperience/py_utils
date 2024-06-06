#!/home/codeknight/.venv/bin/python3

import pkgutil
import importlib
from fire import Fire
def find_and_install_plugin(plugin_name):
    plugins= {}
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_name):
            package = importlib.import_module(name)
            plugins[name] = package

    for _, module in  plugins.items():
        module.run()



if __name__ == "__main__":
    Fire(find_and_install_plugin)
