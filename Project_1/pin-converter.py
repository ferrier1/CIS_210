import argparse

## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz"
VOWELS = "aeiou"



def alphacode(pin):
    letters = []
    while pin > 0:
        x = pin % 100
        vowel = VOWELS[x % 5]
        cons = CONSONANTS[x // 5]
        pin = pin // 100
        letters.extend((vowel, cons))
    letters.reverse()
    return ''.join(letters)




def main():
    parser = argparse.ArgumentParser(description="Enter a PIN")
    parser.add_argument("PIN", type=int, help="an interger to be converted")

    args = parser.parse_args()
    pin = args.PIN

    memorable = alphacode(pin)
    print("Memorable PIN:", memorable)



if __name__ == "__main__":
    main()
