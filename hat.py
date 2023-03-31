# autograde:all-correct a1111 time:2022-10-08T03:15:29+00:00 UTC
def hat(filename, n):
    image = SimpleImage(filename)
   #Let's first create the blanck image that has n pixel greater high. 
   # Then we will copy the picture at the bottom
    out = SimpleImage.blank(image.width, image.height + n)
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x, y)
            pixel_out = out.get_pixel(x, y + n)
            pixel_out.red = pixel.red
            pixel_out.green = pixel.green
            pixel_out.blue = pixel.blue
            
    # Now let's create yellow strip      
    for x in range(image.width):
        for y in range(n):
            pixel_out = out.get_pixel(x, y)
            pixel_out.blue = 0
            pixel_out.red = 255
            pixel_out.green = 255
    return out

