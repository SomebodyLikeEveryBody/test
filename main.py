L_VOWELS = 'aeiouy'
L_ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def get_vowels():
    return [letter for letter in L_ALPHA if letter in L_VOWELS]



def get_consonants():
    return [letter for letter in L_ALPHA if letter not in L_VOWELS]

def print_vowels():
    print(get_vowels())

def print_consonants():
    print(get_consonants())

if (__name__ == "__main__"):
    print_vowels()
    print_consonants()
