# autograde:all-correct a1111 time:2022-11-14T04:16:11+00:00 UTC
def first_nest(strs):
    d={}
    for element in strs:
        Key = element[0]
        Value= element
        
        if Key not in d:
            d[Key]=[]
        d[Key].append(Value)
    return d