import importlib.util


def check_module(module_name):
    """checks if module can be imported without actually importing it"""
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print("module {} not found".format(module_name))
        return None
    else:
        print("module {} can be imported".format(module_name))
        return module_spec


def import_module_from_spec(module_spec):
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    module_spec = check_module("fake_module")
    module_spec = check_module("collections")
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))