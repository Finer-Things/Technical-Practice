def permute_nums(nums, k):
    nums = nums[-k:] + nums[:-k]
    print(nums)
    return nums
print(permute_nums([1,2,3,4,5,6,7], 3))
