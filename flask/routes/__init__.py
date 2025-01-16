import importlib
import os

views = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".py") and f != "__init__.py"]

for view in views:
    importlib.import_module("." + view[:-3], __name__)
    print('App imported ' + view + ' successfully.')