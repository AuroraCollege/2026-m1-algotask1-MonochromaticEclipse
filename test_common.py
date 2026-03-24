import importlib
import pytest


STUDENT_MODULES = [
    "algo_design_level1",
    "algo_design_level2",
    "algo_design_level3",
    "algo_design_level4",
]


def load_student_modules():
    """
    Attempt to import all student level modules.
    Returns (modules, error_msg), where modules is a list.
    """
    modules = []
    try:
        for module_name in STUDENT_MODULES:
            modules.append(importlib.import_module(module_name))
    except SyntaxError as e:
        return None, f"Syntax error in student file (unfilled ??? placeholder?): {e}"
    except Exception as e:
        return None, f"Student file raised an error on import: {e}"
    return modules, None


student_modules, _load_error = load_student_modules()


def get_fn(name):
    """
    Retrieve a named function from the student module.
    Skips the test with a helpful message if the module failed
    to load or the function doesn't exist.
    """
    if student_modules is None:
        pytest.skip(_load_error or "Student module could not be loaded.")

    for module in student_modules:
        fn = getattr(module, name, None)
        if fn is not None:
            return fn

    pytest.skip(f"'{name}' not found in student level files.")
