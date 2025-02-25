import os
import sys
from cx_Freeze import setup, Executable

# Detect all compiled .so/.pyd files in compiled/
compiled_files = [
    (os.path.join("compiled", file), file)
    for file in os.listdir("compiled") if file.endswith((".so", ".pyd"))
]

# Include compiled modules and assets
include_files = [
    ("assets/", "assets/"),  # Include game assets
] + compiled_files  # Add compiled modules

# Dependencies
excludes = ["tkinter", "unittest"]
packages = ["pygame"]

# Define the executable
exe = Executable(
    script="start.py",  # Entry point
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
            "include_msvcr": True
        }
    },
    executables=[exe],
)
