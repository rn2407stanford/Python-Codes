# autograde:all-correct a111 time:2022-10-08T03:14:05+00:00 UTC
def reflect(filename):
    """
    Below I will create blanck image that has a double size
    of the original pic and will it out. Then I will copy all the
    pixels from the original pic into the first half of the blanck pic. 
    """
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width, image.height * 2)
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x, y)
            pixel_top = out.get_pixel(x, y)
            pixel_top.red = pixel.red
            pixel_top.green = pixel.green
            pixel_top.blue = pixel.blue
    """
    Now I will create the opposing side of the image "-y) (mirrored) and 
    then I will drag it down to the bottom with out.height-1
    """
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x, y)
            pixel_mirrored= out.height - y -1
            pixel_bottom = out.get_pixel(x, pixel_mirrored)
            pixel_bottom.red = pixel.red
            pixel_bottom.green = pixel.green
            pixel_bottom.blue = pixel.blue

    return out

