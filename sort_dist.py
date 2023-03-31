# autograde:all-correct a111111 time:2022-11-19T21:56:58+00:00 UTC
def sort_dist(nums, target):
    return sorted(nums, key=lambda nums: abs(nums-target))
