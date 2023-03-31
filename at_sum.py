# autograde:all-correct a111111111 time:2022-10-26T19:10:58+00:00 UTC
def at_sum(s):
    """
    using the find and slicing to return the part we are interested.
    """
    if s.find('@', s.find('@')+1)!=-1:
        sum1=s[s.find('@')+1]
        sum2 = s[s.find('@', s.find('@')+1)+1]
        return int(sum1)+int(sum2)
    return 0
