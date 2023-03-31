# autograde:all-correct a1111111 time:2022-11-14T00:29:33+00:00 UTC
def in_both(a, b):
    Result=[]
    for ch in a:
        if ch in b:
            Result.append(ch)
    return Result
