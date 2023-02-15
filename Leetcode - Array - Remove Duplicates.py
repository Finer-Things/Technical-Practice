class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            j = i
            while nums[j] <= nums[i]:
                j += 1
            if i < n-1:
                nums[i+1] = nums[j]
        return nums


def remove_duplicates(nums):
    n = len(nums)
    j=1
    for i in range(n):
        while nums[j] <= nums[i]:
            if j == n-1:
                return nums[i], nums
            j += 1
        if i < n-1:
            nums[i+1] = nums[j]
    

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))


solution = Solution()
