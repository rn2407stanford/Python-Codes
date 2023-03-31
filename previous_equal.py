# autograde:all-correct a1111111111 time:2022-11-14T04:32:59+00:00 UTC
def previous_equal(nums):
    previous = None
    Result =0
    for num in nums:
        if num==previous:
            Result+=1
        previous=num
    return Result
