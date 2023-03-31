#!/usr/bin/env python3

"""
Stanford CS106A Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):
    """
    Given a key string, compute and return the len-26 slug list for it.
    >>> compute_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> compute_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> compute_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> compute_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    lst = []
    for ch in key:
        if ch.lower() not in lst:
            if ch.isalpha():
                lst.append(ch.lower())

    for ch in ALPHABET:
        if ch not in lst:
            lst.append(ch)
    return lst


def encrypt_char(source, slug, ch):
    """
    Given source and slug lists,
    if the char ch is in source, return
    its encrypted form. Otherwise return ch unchanged.
    >>> # Compute 'z' slug, store it in a var named z_slug
    >>> # and pass that in as the slug for the tests.
    >>> z_slug = compute_slug('z')
    >>> encrypt_char(ALPHABET, z_slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, z_slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, z_slug, 'D')
    'C'
    >>> encrypt_char(ALPHABET, z_slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, z_slug, ' ')
    ' '
    """
    slug = compute_slug(slug)
    if ch in source:
        return slug[source.index(ch)]
    elif ch.lower() in source:
        return slug[source.index(ch.lower())].upper()
    return ch


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> z_slug = compute_slug('z')
    >>> encrypt_str(ALPHABET, z_slug, 'And like a thunderbolt he falls.')
    'Zmc khjd z sgtmcdqanks gd ezkkr.'
    """
    result = ''
    for ch in s:
        char = encrypt_char(source, slug, ch)
        result += char
    return result


def decrypt_str(source, slug, s):
    """
    Given source and slug lists and encrypted string s,
    return the decrypted form of s.
    >>> z_slug = compute_slug('z')
    >>> decrypt_str(ALPHABET, z_slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.')
    'And like a thunderbolt he falls.'
    """
    return encrypt_str(slug, source, s)


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as filename:
        for line in filename:
            print(encrypt_str(ALPHABET, slug, line), end='')



def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    slug = compute_slug(key)
    with open(filename) as filename:
        for line in filename:
            print(decrypt_str(ALPHABET, slug, line), end='')


def main():
    args = sys.argv[1:]

    if len(args) == 3 and args[0] == '-encrypt':
        print(encrypt_file(args[2], args[1]))

    if len(args) == 3 and args[0] == '-decrypt':
        print(decrypt_file(args[2], args[1]))
    # 2 command line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.




# Python boilerplate.
if __name__ == '__main__':
    main()
