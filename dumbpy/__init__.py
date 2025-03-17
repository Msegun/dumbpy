import sys
import argparse


def run_dumbpy() -> None:
    parser = argparse.ArgumentParser(description='Hello. Thank you for using DumbPy')
    _ = parser.parse_args()
    try:
        pass # Run the DumbPy lint process
    except KeyboardInterrupt:
        sys.exit(1)
