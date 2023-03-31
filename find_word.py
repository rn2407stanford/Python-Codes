# autograde:all-correct a111111111 time:2022-09-05T00:51:59+00:00 UTC
def find_word(s):
    if s=='':
        return None
    start=0
    while not s[start].isalpha():
        start+=1
    end=start+1
    while end<len(s) and (s[end].isalpha() or s[end].isdigit()):
        end+=1
    return s[start:end]
    