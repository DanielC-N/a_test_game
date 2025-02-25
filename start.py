import os
import sys
import importlib

# Detect if running inside a frozen binary (cx_Freeze)
if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS  # Path where cx_Freeze extracts files
else:
    base_dir = os.path.abspath("compiled")

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
