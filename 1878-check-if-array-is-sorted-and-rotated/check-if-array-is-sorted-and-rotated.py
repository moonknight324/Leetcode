class Solution:
    def check(self, nums: list[int]) -> bool:
        if nums == sorted(nums):
            return True
        rotated = []
        for i in range(len(nums)):
            rotated = nums[i:] + nums[:i]
            if rotated == sorted(nums):
                return True
        return False
        