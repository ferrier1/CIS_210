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


def strcode(word):
    for letter in word:
        vlist = list(VOWELS)
        clist = list(CONSONANTS)
        if letter in vlist:
            print(vlist.index(letter))
        else:
            print(clist.index(letter) % 10)



def main():
    parser = argparse.ArgumentParser(description="Enter a PIN")
    parser.add_argument("-P", metavar="PIN", type=int, help="an interger to be converted")
    parser.add_argument("-S", type=str, metavar="STRING", help="a string to be converted")

    args = parser.parse_args()
    pin = args.P
    word = args.S

    if pin != None:
        memorable = alphacode(pin)
        print("Memorable PIN:", memorable)
    elif word != None:
        strcode(word)
    else:
        print("invalid input")




if __name__ == "__main__":
    main()
