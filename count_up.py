# autograde:all-correct a11111111 time:2022-10-26T19:09:03+00:00 UTC
def count_up(s):
    result=0
    """
    for i in range(len(s)):
        if s[i].isupper():
            result +=1
    return result
    """
    
    for ch in s:
        if ch.isupper():
            result +=1
    return result
