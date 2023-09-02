"""
On a terminal, run using below command.

python hello_world.py ["optional string argument that you want the program to print"]
"""

import sys

argv = sys.argv

try:
    print(argv[1])

except:
    print("Hello, everyone! Welcome to Python crash course with Joshy Dev. 😀")