# autograde:all-correct a1111111111 time:2022-10-26T19:08:39+00:00 UTC
def find_plus(s):
    """
    Using find function to find what we need-two times
    then slice s and return
    """
    if s.find('+', s.find('+') +1 ) != -1:
        s_first=s.find('+')
        s_second = s.find('+', s_first+1)
        return s[s_first+1: s_second]
    return ''
