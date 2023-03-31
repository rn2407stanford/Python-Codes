# autograde:all-correct a11111111111 time:2022-10-02T00:19:26+00:00 UTC
def move_until_blocked(bit):
    while bit.front_clear():
        bit.move()

def red_until_blocked(bit):
    bit.paint('red')
    while bit.front_clear():
        bit.move()
        bit.paint('red')

def half_s(bit):
    while bit.front_clear():
        red_until_blocked(bit)
    bit.right()
    while bit.front_clear():
        red_until_blocked(bit)
    bit.left()
    bit.left()
    move_until_blocked(bit)
    bit.left()
    move_until_blocked(bit)
    bit.left()
    bit.left()
    
def big_red(filename):
    bit = Bit(filename)
    while bit.front_clear():
        bit.move()
        if bit.get_color()=='green':
            bit.left()
            half_s(bit)
            bit.right()
            bit.move()
            bit.right()
            half_s(bit)
            bit.left()
            