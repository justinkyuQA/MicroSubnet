import sys

from .core import calculate

HELP = """
MicroSubnet v0.1

Usage

python3 -m microsubnet <CIDR>

Example

python3 -m microsubnet 192.168.1.0/24
"""

def main():

    args = sys.argv[1:]

    if not args:
        print(HELP)
        return

    calculate(args[0])
