# Shelling and transcoding to C
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["system.py"]),
)
# py2 shell.py build_ext --inplace
