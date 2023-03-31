# autograde:all-correct a111 time:2022-10-01T20:33:02+00:00 UTC
def cave_blue(filename):
    bit = Bit(filename)
    while not bit.get_color()=='red':
        bit.move()
    bit.right()
    bit.move()
    while not bit.right_clear():
        bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
