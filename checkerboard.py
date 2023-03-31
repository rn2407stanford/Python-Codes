# autograde:all-correct a111111 time:2022-10-02T00:20:44+00:00 UTC
def do_one1(bit):
    bit.left()
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        if bit.front_clear():
            bit.move()
            bit.paint('blue')
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    
def do_one2(bit):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
        if bit.front_clear():
            bit.move()
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    
    
def do_checkerboard(filename):
    """
    Starts at the north west corner facing south. Moves south
    completeing the checkerboard rows. Ends in the botoom
    row facing south.
    """
    bit = Bit(filename)
    do_one1(bit)
    while bit.front_clear():
        bit.move()
        do_one2(bit)
        if bit.front_clear():
            bit.move()
            do_one1(bit)

    

