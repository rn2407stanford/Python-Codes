# autograde:all-correct a1111111 time:2022-10-26T19:11:09+00:00 UTC
def first_alpha(s):
    """
    for i in range(len(s)):
        if s[i].isalpha():
            return i
    return -1
    """
    for ch in s:
        if ch.isalpha():
            return s.find(ch)
    return -1
