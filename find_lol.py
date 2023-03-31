# autograde:all-correct a11111111111 time:2022-11-06T04:47:51+00:00 UTC
def find_lol(s):
    LOL=s.find('LOL')
    if LOL==-1:
        return ''
    
    start=LOL-1
    while start>=0 and s[start].isalpha() or s[start]==' ':
        start -= 1

    return s[start+1: LOL+3]
