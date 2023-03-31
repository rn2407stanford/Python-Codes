# autograde:all-correct a11111 time:2022-10-01T20:34:14+00:00 UTC
def top_bluegreen(filename):
    bit = Bit(filename)
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        bit.paint('green')
        if bit.front_clear():
            bit.move()
            bit.paint('blue')
