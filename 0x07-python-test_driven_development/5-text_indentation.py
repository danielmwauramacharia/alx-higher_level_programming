#!/usr/bin/python3
"""Working with multiline string"""


def text_indentation(text=""):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    words = text.split()
    for i, word in enumerate(words):
        if word.endswith(('.', ':', '?')):
            print(word)
            for _ in range(1):
                print()
        elif any(chr in ('.', '?', ':') for chr in word):
            for cha in word:
                print(cha, end='')
                if cha in ('.', '?', ':'):
                    for _ in range(2):
                        print()
        else:
            print(word, end='')
            if i < len(words) - 1:
                print(' ', end='')
