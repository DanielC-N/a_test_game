import os
import sys
from cx_Freeze import setup, Executable

# Define game assets and compiled modules to include
include_files = [
    ("assets/", "assets/"),   # Include all assets
    ("compiled/", "compiled/"),  # Include all compiled Cython files
]

# Dependencies
excludes = ["tkinter", "unittest"]
packages = ["pygame"]

# Define the executable
exe = Executable(
    script="start.py",  # Entry point for the compiled game
    base="Win32GUI" if sys.platform == "win32" else None,
    target_name="game",
    icon="assets/logo.ico" if sys.platform == "win32" else "assets/logo.png",
)

setup(
    name="My Little Game",
    version="1.0",
    description="A fun little game built with pygame",
    options={
        "build_exe": {
            "packages": packages,
            "excludes": excludes,
            "include_files": include_files,
            "include_msvcr": True  # Ensure Windows users get runtime DLLs
        }
    },
    executables=[exe],
)
