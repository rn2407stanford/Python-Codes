# autograde:all-correct a111111 time:2022-11-19T21:59:03+00:00 UTC
def max_dist(nums, target):
    return max(nums, key=lambda nums: abs(nums-target))
