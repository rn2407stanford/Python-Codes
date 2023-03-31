# autograde:all-correct a1111111111 time:2022-09-04T22:37:25+00:00 UTC
def find_binary(s):
    start=s.find('#b')
    end= start +2
    
    while end < len(s) and (s[end] is '1' or s[end] is '0'):
        end+=1
    return s[start:end]