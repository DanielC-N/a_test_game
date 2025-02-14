import os
import sys
from cx_Freeze import setup, Executable

THE_LOGO="assets/logo.ico"

# Automatically detect all files in the 'assets' directory
def find_extra_files(directory):
    extra_files = []
    for folder, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(folder, file)
            extra_files.append(file_path)
    return extra_files

# Extra files to include (Modify this if you have more folders)
include_files = [
  THE_LOGO,  # Ensure logo is included
] + find_extra_files("assets")  # Include all files from 'assets' directory

# Dependencies
excludes = ["tkinter", "unittest"]
packages = ["pygame"]

# Define the executable file
exe = Executable(
    script="main.py",
    base="Win32GUI" if sys.platform == "win32" else None,
    target_name="game",
    icon=THE_LOGO
)

# Setup configuration
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
    executables=[exe]
)
