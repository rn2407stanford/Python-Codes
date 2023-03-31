# autograde:all-correct a1111 time:2022-10-08T03:16:14+00:00 UTC
def purple(filename, margin):
    image = SimpleImage(filename)
    
    # Lets create blank image bigger size and then place the pic at the center
    out = SimpleImage.blank(image.width + 2*margin, image.height)
    for x in range(image.width):
        for y in range(image.height):
            pixel=image.get_pixel(x, y)
            pixel_out = out.get_pixel(x + margin, y)
            pixel_out.red = pixel.red
            pixel_out.green = pixel.green
            pixel_out.blue = pixel.blue
            
    # Now let's create purple strip left      
    for y in range(image.height):
        for x in range(margin):
            pixel_out = out.get_pixel(x, y)
            pixel_out.green = 0
    # Now let's create purple strip right      
    for y in range(image.height):
        for x in range(margin):
            pixel_out = out.get_pixel(x + margin + image.width, y)
            pixel_out.green = 0
    return out

