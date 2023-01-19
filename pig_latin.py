#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Dec 2022
# This program converts the sentence to Pig Latin


def pig_latin(sentence):
    # This function converts normal text to Pig Latin
    new_words = []
    words = sentence.split()

    # conversion
    for word in words:
        new_word = "{0}{1}ay".format(word[1:], word[0])
        new_words.append(new_word)

    # joining strings
    new_sentence = " ".join(new_words).lower()

    return new_sentence


def main():
    # This function is the main function
    print("Pig Latin Converter")

    # input
    user_input = input("Enter a sentence: ")

    # process & output
    print("\n{0}".format(pig_latin(user_input)))

    print("\nDone.")


if __name__ == "__main__":
    main()
