import os
import sys
import importlib

# Add "compiled/" directory to Python’s search path
sys.path.insert(0, os.path.abspath("compiled"))

# Try to import the compiled "main" module
try:
    main = importlib.import_module("main")
except ModuleNotFoundError:
    raise ImportError("Failed to load the compiled game. Make sure you compiled it using setup_c.py.")

# Run the game
if hasattr(main, "run_game"):
    main.run_game()
else:
    raise ImportError("The function 'run_game()' is missing in the compiled module.")
