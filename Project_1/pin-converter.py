import argparse



def alphacode(pin):
    while pin > 0:
        x = pin % 100
        print(x)
        pin = pin // 100


def main():
    parser = argparse.ArgumentParser(description="Enter a PIN")
    parser.add_argument("PIN", type=int, help="an interger to be converted")

    args = parser.parse_args()
    pin = args.PIN



if __name__ == "__main__":
    main()     #FIXME: Uncomment this when your program is working
