#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((1, 1, 1), (6.6, 6.2, 12.4))
    188.36
    >>> pix_dist2((2, 0, 1), (6.6, 6.2, 12.4))
    189.56
    """
    return sum(list(map(lambda i, j: (abs(i-j)**2), pix1, pix2)))

def average_pix(pixs):
    """
    Given list of 1 or more pix, returns the average pix.
    >>> average_pix([(1, 1, 1), (1, 1, 31), (28, 28, 28)])
    (10.0, 10.0, 20.0)
    >>> average_pix([(1, 1, 1), (1, 1, 31), (28, 28, 28), (3, 3, 9)])
    (8.25, 8.25, 17.25)
    >>> average_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28), (2, 0, 1), (1, 1, 31)] )
    (6.6, 6.2, 12.4)
    >>> average_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28), (2, 0, 1), (1, 0, 2) ] )
    (6.6, 6.0, 6.6)
    """
    return tuple(map(lambda n: sum(n) / float(len(n)), zip(*pixs)))


def best_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.
    >>> best_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28)] )
    (1, 1, 1)
    >>> best_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28), (2, 0, 1), (1, 1, 31)] )
    (1, 1, 1)
    """
    mean = average_pix(pixs)
   # return min(pixs, key= lambda pixs: abs(pixs[0]-mean[0])**2
    #                                   + abs(pixs[1]-mean[1])**2 +abs(pixs[2]-mean[2])**2)
    return min(pixs, key=lambda pixs: pix_dist2(pixs, mean))


def good_apple_pix(pixs):
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (20, 20, 20)
    """
    mean = average_pix(pixs)
    sorted_pix=sorted(pixs, key=lambda pixs: pix_dist2(pixs, mean))
    midpoint=len(sorted_pix)//2
    Good_list = sorted_pix[0:midpoint]
    mean_good=average_pix(Good_list)
    best= min(Good_list, key=lambda Good_list: pix_dist2(Good_list, mean_good))
    # we can also use best_pix(Good_list)
    return best

def pixs_at_xy(images, x, y):
   """
   Takes in the list of images and an x,y, returns a list of all the pix at that x,y
   """
   pixs=[]
   for image in images:
       pix = image.get_pix(x, y)
       pixs.append(pix)
   return pixs


def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """
    width = images[0].width
    height = images[0].height
    solution = SimpleImage.blank(width, height)
    for x in range(solution.width): # Notice here all the images/solution have the same size
        for y in range(solution.height):
            pixs=pixs_at_xy(images, x, y)
            if mode == None:
                pix=best_pix(pixs)
            if mode == '-good':
                pix=good_apple_pix(pixs)
            solution.set_pix(x, y, pix)
    solution.show()



def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == '-good':
        images = load_images(args[1])
        solve(images, '-good')


if __name__ == '__main__':
    main()
