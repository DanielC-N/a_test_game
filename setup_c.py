import os
import shutil
from setuptools import setup, Extension
from Cython.Build import cythonize

# Find all .py files in src/
def find_py_files(directory):
    return [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".py") and file not in ["__init__.py"]
    ]

# Compile all Python files as separate extensions
extensions = [
    Extension(
        name=os.path.splitext(os.path.basename(file))[0],  # Keep module name clean
        sources=[file],
    )
    for file in find_py_files("src")
]

setup(
    name="MyGame",
    version="1.0",
    description="A compiled game built with pygame",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
)

# Move compiled files to "compiled/" directory and rename them
os.makedirs("compiled", exist_ok=True)
for file in os.listdir():
    if file.endswith(".so") or file.endswith(".pyd"):
        new_name = file.split(".cpython")[0] + ".so"  # Strip cpython-XXX-ARCH
        print(f"Renaming {file} to compiled/{new_name}")
        shutil.move(file, f"compiled/{new_name}")
