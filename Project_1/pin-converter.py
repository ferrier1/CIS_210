import argparse
import numpy

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
    raw_list = []
    fin_list = []
    for letter in word:
        vlist = list(VOWELS)
        clist = list(CONSONANTS)
        if letter in vlist:
            v = vlist.index(letter)
            raw_list.append(v)
        else:
            c = clist.index(letter)
            raw_list.append(c)
    if len(raw_list) % 2 != 0:
        [0] + raw_list
    raw_join = ''.join(str(digit) for digit in raw_list)
    n = len(raw_list) // 2
    l = numpy.array_split(raw_list, n)
    for grp in l:
        x = grp[0] * 5 + grp[1]
        fin_list.append(x)
    return ''.join(str(digit) for digit in fin_list)





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
        print("Decoded PIN:", strcode(word))
    else:
        print("invalid input")



if __name__ == "__main__":
    main()
