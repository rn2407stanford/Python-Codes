# autograde:all-correct a111111 time:2022-10-26T19:13:16+00:00 UTC
def alpha_list(s):
    """ 
    Using isalpha and append to find what we are interested
    """
    lst=[]
    for i in range(len(s)):
        if s[i].isalpha():
            lst.append(s[i])
    return lst