# Modifies system path to allow main.py to import from the Nowhere package
# Author: William Kluge
# Date: 2017-10-25

import sys

if __name__ == "__main__":
    # If this script is called, show the changes being made to the path
    print("Old path:", sys.path)
    sys.path.append("..")
    print("New path:", sys.path)
else:
    # If this script is just being called (when it is imported), just append to the path silently
    sys.path.append("..")
