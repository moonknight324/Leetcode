class Solution:
    def check(self, nums: list[int]) -> bool:
        target = sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == target:
                return True
        return False
        