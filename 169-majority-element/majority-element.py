class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        majority = len(nums) / 2
        for key,val in freq.items():
            if val > majority:
                return key