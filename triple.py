# autograde:all-correct a1111 time:2022-08-17T04:52:49+00:00 UTC
def do_one(bit):
    while not bit.left_clear():
        bit.paint('green')
        bit.move()
    bit.left()
    bit.move()
    while not bit.left_clear():
        bit.paint('green')
        bit.move()
    bit.left()
    bit.move()
    while not bit.left_clear():
        bit.paint('green')
        bit.move()



def do_triple(filename):
    """
    Bit starts facing along the first side.
    Solves the triple problem, moving through
    3 rectangles.
    """
    bit = Bit(filename)
    do_one(bit)
    bit.right()
    do_one(bit)
    bit.right()
    do_one(bit)









