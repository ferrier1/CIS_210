import argparse

## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz"
VOWELS = "aeiou"



def alphacode(pin):
    while pin > 0:
        x = pin % 100
        #print(x)
        #print("----")
        vowel = VOWELS[x % 5]
        print(vowel)
        #print("----")
        cons = CONSONANTS[x // 5]
        print(cons)
        #print("----")
        pin = pin // 100
        #print("----")



def main():
    parser = argparse.ArgumentParser(description="Enter a PIN")
    parser.add_argument("PIN", type=int, help="an interger to be converted")

    args = parser.parse_args()
    pin = args.PIN

    memorable = alphacode(pin)



if __name__ == "__main__":
    main()
