# autograde:all-correct a1111 time:2022-10-01T20:18:16+00:00 UTC
def go_hide(filename):
    bit = Bit(filename)
    while not bit.right_clear():
        bit.move()
    pass
    bit.right()
    while bit.front_clear():
       bit.move()
