import importlib.util
import os

def load_module(path):
    spec = importlib.util.spec_from_file_location(os.path.splitext(os.path.basename(path))[0], path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo