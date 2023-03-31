#!/usr/bin/env python3

"""
Stanford CS106A TipTop Project
"""

import sys

def make_dict(filename):
    """
    Reads the text file into a dictionary having a key for each tag and list of posters of posted with that tag.
    >>> make_dict('test1.txt')
    {'#aaa': ['@bob', '@alice'], '#bbb': ['@bob', '@alice']}
    >>> make_dict('test2.txt')
    {'#bbb': ['@alice', '@bob'], '#aaa': ['@alice', '@bob', '@aardvark'], '#z': ['@bob']}
    """
    with open(filename) as f:
        lines=f.readlines()
    lines=list(map(lambda n: n.lower(), lines))
    tags=[]
    dic={}
    for line in lines:
        line = line.strip('\n')
        line = line.split('^')
        for tag in line[1:]:
            if tag not in tags:
                tags.append(tag)

    for tag in tags:
        dic[tag]=[]

        for line in lines:
            if tag in line:
                poster=line[:line.find('^')]
                if poster not in dic[tag]:
                    dic[tag].append(poster) #The list of posters should not have duplicates in it.
    return dic


def make_print(dic):
    """    
    Prints dic's keys followed by values of that key in alphabetical order. Values indented by 1 space:

    >>> make_print({'#bbb': ['@alice', '@bob'], '#aaa': ['@alice', '@bob', '@aardvark'], '#z': ['@bob']})
    #aaa
     @aardvark
     @alice
     @bob
    #bbb
     @alice
     @bob
    #z
     @bob
    """
    for word in sorted(dic.keys()):
        print(word)
        for poster in sorted(dic[word]):
            print(" "+ poster)


def main():
    args = sys.argv[1:]

    if len(args) == 1:
        dic=make_dict(args[0])
        make_print(dic)

if __name__ == '__main__':
    main()