#!/usr/bin/env python
import sys


def read_words(filename):
    lookup = {}
    with open(filename, "r") as f:
        line = f.readline()
        while line:
            word = line.replace('\n', '')
            key = word_hash(word)
            if key in lookup:
                lookup[key].append(word)
            else:
                lookup[key] = [word]
            line = f.readline()
    return lookup


def word_hash(word):
    counter = [0] * 27
    for ch in word:
        counter[get_index(ch.lower())] += 1
    return tuple(counter)


def get_index(ch):
    return 26 if ch == '-' else ord(ch) - ord('a')


def get_anagram(chars, lookup):
    key = word_hash(chars)
    return lookup[key] if key in lookup else []


def do_test(st, lookup):
    arr = []
    print('test case: ' + st)
    for ch in st:
        if ch.isalpha() or ch == '-':
            arr.append(ch)
        else:
            print('Invalid character found')
            return
    print('result: ' + str(get_anagram(arr, lookup)))


if __name__ == "__main__":
    dict_filename = sys.argv[1]
    test_filename = sys.argv[2]
    print('generating lookup table...')
    lookup = read_words(dict_filename)
    with open(test_filename) as f:
        line = f.readline().replace('\n', '')
        while line:
            do_test(line, lookup)
            line = f.readline().replace('\n', '')
