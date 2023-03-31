# autograde:all-correct a111 time:2022-10-01T20:08:25+00:00 UTC
def top_logic1(filename):
    bit = Bit(filename)
    while bit.front_clear():
        bit.move()
        if bit.get_color()=='red':
            bit.paint('green')