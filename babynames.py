#!/usr/bin/env python3

"""
Stanford CS106A BabyNames Project
Part-A: organizing the bulk data
"""

import sys


def add_name(names, year, rank, name):
    """
    Add the given data: int year, int rank, str name
    to the given names dict and return it.
    (1 test provided, more tests TBD)
    >>> add_name({}, 2000, 10, 'Abe')
    {'Abe': {2000: 10}}
    >>> add_name({'Aaden': {2010: 560}}, 2010, 56, 'Aaliyah')
    {'Aaden': {2010: 560}, 'Aaliyah': {2010: 56}}
    >>> add_name({'Aaden': {2010: 560}, 'Aaliyah': {2010: 56}}, 2010, 56, 'Richard')
    {'Aaden': {2010: 560}, 'Aaliyah': {2010: 56}, 'Richard': {2010: 56}}
    >>> add_name({'Aaden': {2000: 560}, 'Christian': {2000: 22}}, 2000, 576, 'Christian')
    {'Aaden': {2000: 560}, 'Christian': {2000: 22}}
    >>> add_name({'Aaden': {2000: 560}, 'Christian': {2000: 22, 2007: 57}}, 2010, 576, 'Christian')
    {'Aaden': {2000: 560}, 'Christian': {2000: 22, 2007: 57, 2010: 576}}
    """
    d0={}
    d0[year]=rank
    d={}
    d.update(names)
    if name in d:
        small_d = d[name]
        if year in d[name]:
            if small_d[year] > rank:
                small_d[year] = rank
        else:
            small_d.update(d0)
    else:
        d[name]=d0
    return d


def add_file(names, filename):
    """
    Given a names dict and babydata.txt filename, add the file's data
    to the dict and return it.
    (Tests provided, Code TBD)
    >>> add_file({}, 'small-2000.txt')
    {'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}
    >>> add_file({}, 'small-2010.txt')
    {'Yot': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Alice': {2010: 2}}
    >>> add_file({'Bob': {2000: 1}, 'Alice': {2000: 1}, 'Cindy': {2000: 2}}, 'small-2010.txt')
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    f=open(filename)
    lines=f.readlines()
    year=lines[0].strip('\n')
    year=int(year)
    for line in lines[1:]:
        line=line.strip('\n')
        line=line.split(',')
        rank=int(line[0])
        name1=line[1]
        f1=add_name(names, year, rank, name1)
        name2 = line[2]
        f2=add_name(f1, year, rank, name2)
        names=f2
    return f2


def read_files(filenames):
    """
    Given list of filenames, build and return a names dict
    of all their data.
    >>> read_files(['small-2000.txt', 'small-2010.txt'])
    {'Bob': {2000: 1, 2010: 2}, 'Alice': {2000: 1, 2010: 2}, 'Cindy': {2000: 2}, 'Yot': {2010: 1}, 'Zena': {2010: 1}}
    """
    name = {}
    for filename in filenames:
        add= add_file(name, filename)
        name=add
    return add


def search_names(names, target):
    """
    Given names dict and a target string,
    return a sorted list of all the name strings
    that contain that target string anywhere.
    Not case sensitive.
    (Code and tests TBD)
    >>> search_names({'Aaliyah': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Ayaan': {2010: 2}}, 'aa')
    ['Aaliyah', 'Ayaan']
    >>> search_names({'Aaliyah': {2010: 1}, 'Zena': {2010: 1}, 'Bob': {2010: 2}, 'Ayaan': {2010: 2}}, 'AA')
    ['Aaliyah', 'Ayaan']
    >>> search_names({'Aaden': {2000: 560}, 'Christian': {2000: 22, 2007: 57}}, 'aa')
    ['Aaden']
    >>> search_names({'Aaden': {2000: 560}, 'Christian': {2000: 22, 2007: 57}}, 'lm')
    []
    """
    target=target.lower()
    Result=[]
    list=[]
    for key in names.keys():
        list.append(key)
    for name in list:
        if name.lower().find(target) != -1:
            Result.append(name)
    Result=sorted(Result)
    return Result


def print_names(names):
    """
    (provided)
    Given names dict, print out all its data, one name per line.
    The names are printed in increasing alphabetical order,
    with its years data also in increasing order, like:
    Aaden [(2010, 560)]
    Aaliyah [(2000, 211), (2010, 56)]
    ...
    Surprisingly, this can be done with 2 lines of code.
    We'll explore this in lecture.
    """
    for key, value in sorted(names.items()):
        print(key, sorted(value.items()))


def main():
    # (provided)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Change filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
