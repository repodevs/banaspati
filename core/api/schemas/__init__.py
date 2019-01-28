import os
import json


def load_schema(name, path=None):
    module_path = os.path.dirname(__file__)
    path = os.path.join(module_path, path or '', '{}.json'.format(name))

    with open(os.path.abspath(path), 'r') as fp:
        data = fp.read()

    return json.loads(data)
