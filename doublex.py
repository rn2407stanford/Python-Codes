# autograde:all-correct a11111 time:2022-11-14T00:26:44+00:00 UTC
def doublex(strs):
    Result=[]
    for i in range(len(strs)):
        if strs[i].find("x") != -1:
            Result+=""
        else:
            Result.append(strs[i]+strs[i])
    return Result

