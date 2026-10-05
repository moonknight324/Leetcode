class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return nums

        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        items = sorted(freq.items(), key=lambda item: item[1])

        res = []
        n = len(items)
        for i in range(k):
            res.append(items[n - i - 1][0]) 
        return res