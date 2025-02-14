import os
import shutil
from setuptools import setup, Extension
from Cython.Build import cythonize

# Find all .py files in src/
def find_py_files(directory):
    py_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                py_files.append(full_path)
    return py_files

# Convert all Python files to compiled C extensions
extensions = [
    Extension(
        name=os.path.splitext(os.path.relpath(file, "src"))[0].replace(os.sep, "."),
        sources=[file],
    )
    for file in find_py_files("src")
]

c_directives = {
    "language_level": "3",
    "boundscheck": False,
    "wraparound": False,
    "cdivision": True
}

setup(
    name="MyGame",
    version="1.0",
    description="A game built with pygame",
    ext_modules=cythonize(extensions, compiler_directives=c_directives),
)

for file in os.listdir():
    if file.endswith(".so") or file.endswith(".pyd"):
        new_name = file.split(".cpython")[0] + os.path.splitext(file)[-1]  # Remove 'cpython-xxx'
        print(f"Moving {file} to src/{new_name}")
        shutil.move(file, f"src/{new_name}")