import os
import sys
import importlib

# Detect if running inside a frozen executable (cx_Freeze)
if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)  # cx_Freeze extracts files here
else:
    base_dir = os.path.abspath("compiled")  # Running normally

sys.path.insert(0, base_dir)

# Try to import the compiled "main" module
try:
    main = importlib.import_module("main")
except ModuleNotFoundError:
    raise ImportError(f"Failed to load the compiled game from {base_dir}. Ensure you compiled it using setup_c.py.")

# Run the game
if hasattr(main, "run_game"):
    main.run_game()
else:
    raise ImportError("The function 'run_game()' is missing in the compiled module.")
