# autograde:all-correct a11111 time:2022-11-14T02:48:34+00:00 UTC
def first_counts(strs):
    Key=[]
    for i in range(len(strs)):
        if strs[i]!='':
            element=strs[i]
            Key.append(element[0])
    
    counts={}
    for s in Key:
        if s not in counts:
            counts[s] =0
        counts[s] += 1
    return counts