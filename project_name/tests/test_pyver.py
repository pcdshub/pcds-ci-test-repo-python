import sys

def test_is_py39():
    if (3, 9) <= sys.version_info < (3, 10):
        return
    raise RuntimeError('Not py39')
