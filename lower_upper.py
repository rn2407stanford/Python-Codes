# autograde:all-correct a1111111 time:2022-10-26T19:11:32+00:00 UTC
def lower_upper(s):
    result=''
    """
    for i in range(len(s)):
        if s[i].islower():
            result+= s[i]
    for i in range(len(s)):
        if s[i].isupper():
            result+= s[i]
    return result
    """
    
    for ch in s:
        if ch.islower():
            result+=ch
    for ch in s:
        if ch.isupper():
            result+= ch
    return result