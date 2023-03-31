# autograde:all-correct a111 time:2022-10-01T20:08:45+00:00 UTC
def top_logic2(filename):
    bit = Bit(filename)
    while bit.front_clear():
        bit.move()
        if bit.get_color() != 'blue':
            bit.paint('green')
