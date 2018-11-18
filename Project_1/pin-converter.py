import argparse

parser = argparse.ArgumentParser(description="Enter a PIN")
parser.add_argument("PIN", type=int, help="an interger to be converted")

args = parser.parse_args()
print(args.PIN)
