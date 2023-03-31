# autograde:all-correct a1111 time:2022-10-01T20:07:55+00:00 UTC
def top_bot(filename):
    bit = Bit(filename)
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        bit.paint('blue')
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.paint('green')
    while bit.front_clear():
        bit.move()
        bit.paint('green')


