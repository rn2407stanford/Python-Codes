# autograde:all-correct a1111111 time:2022-10-26T19:15:59+00:00 UTC
def food_index(foods):
    """
    we are returning -1 with return -1 function
    """
    if 'coffee' in foods:
        return foods.index('coffee')
    elif 'donut' in foods:
        return foods.index('donut')
    return -1
