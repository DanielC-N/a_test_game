import os
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

# Function to find all Python files in "src" folder
def find_py_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                py_files.append(full_path)
    return py_files

# Convert all .py files in src/ to compiled extensions
extensions = [
    Extension(
        name=os.path.splitext(os.path.relpath(file, "src"))[0].replace(os.sep, "."),
        sources=[file],
    )
    for file in find_py_files("src")
]

setup(
    name="MyGame",
    version="1.0",
    description="A game built with pygame",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3", "boundscheck": False, "wraparound": False, "cdivision": True}),
)
