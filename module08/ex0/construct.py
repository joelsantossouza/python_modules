import sys
from site import getsitepackages
from sys import base_prefix, prefix
from os.path import basename


if __name__ == "__main__":
    # In older python verions, if exist the attribute
    # 'real_prefix', that would mean is inside a virtual environment
    # (first part of if condition). But for newer versions, we compare the base
    # prefix (dir where python is installed), with the prefix (current python
    # environment location). If prefix is not the base_prefix, it means that
    # now it holds the path of a virtual environment
    if hasattr(sys, 'real_prefix') or \
            (hasattr(sys, 'base_prefix') and base_prefix != prefix):
        print(
            "\nMATRIX STATUS: Welcome to the construct\n\n"
            f"Current Python: {sys.executable}\n"  # Path of current executable
            f"Virtual Environment: {basename(prefix)}\n"  # Name of environment
            f"Environment Path: {prefix}\n\n"  # Path of environment
            f"SUCCESS: You're in an isolated environment!\n"
            f"Safe to install packages without affecting\n"
            f"the global system.\n\n"
            f"Package installation path:\n"
            f"{getsitepackages()}"  # Installed packages (pip) are stored here
        )
    else:
        print(
            "\nMATRIX STATUS: You're still plugged in\n\n"
            f"Current Python: {sys.executable}\n"
            "Virtual Environment: None detected\n\n"
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n\n"
            "To enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\n"
            "Scripts\n"
            "activate    # On Windows\n\n"
            "Then run this program again."
        )
