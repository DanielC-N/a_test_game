import os
import sys
import importlib

# Add the "src" folder to Python’s module search path
sys.path.insert(0, os.path.abspath("src"))

# Try importing the compiled Cython module
try:
    main = importlib.import_module("main")
except ModuleNotFoundError:
    raise ImportError("Failed to load the compiled module. Make sure you ran setup_c.py.")

# Run your game
main.run_game()
