"""
Purpose of module is to provide compatibility between Python 2 and 3.
"""

import sys

IS_PYTHON_3 = sys.version_info[0] == 3

if not IS_PYTHON_3:
    BUILTIN = '__builtin__'
else:
    BUILTIN = 'builtins'
