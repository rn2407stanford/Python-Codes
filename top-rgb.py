# autograde:all-correct a1111 time:2022-10-01T20:05:48+00:00 UTC
def top_rgb(filename):
    bit = Bit(filename)
    bit.paint('red')
    while bit.front_clear():
        bit.move()
        bit.paint('green')
    bit.paint('blue')
