# autograde:all-correct a11111 time:2022-10-26T19:11:21+00:00 UTC
def char_misc(s):
    result=''
    #for i in range(len(s)):
    #    if not s[i].isalpha() and not s[i].isdigit():
    #        result += s[i]
    # return result
    
    for ch in s:
        if not ch.isalpha() and not ch.isdigit():
            result += ch
    return result

