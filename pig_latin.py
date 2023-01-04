#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Jan 2022
# This program translates english to pig latin


def main():
    # This function translates pig latin

    ay = "ay"
    way = "way"
    consonant = (
        "B",
        "C",
        "D",
        "F",
        "G",
        "H",
        "J",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "Y",
        "V",
        "X",
        "Z",
    )
    vowel = ("A", "E", "I", "O", "U")

    user_word = input("What word would you like to translate to pig latin: ")

    first_letter = user_word[0]
    first_letter = str(first_letter)
    first_letter = first_letter.upper()
    if first_letter in consonant:
        length_of_word = len(user_word)
        remove_first_letter = user_word[1:length_of_word]
        pig_latin = remove_first_letter + first_letter + ay
        print("Your word translated to pig latin is:", pig_latin)
    elif first_letter in vowel:
        pig_latin = user_word + way
        print("The word in Pig Latin is:", pig_latin)
    else:
        print("Invalid Input.")


if __name__ == "__main__":
    main()
