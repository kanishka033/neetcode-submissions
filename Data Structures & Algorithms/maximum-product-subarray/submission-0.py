class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        max_end = 1
        min_end = 1

        for i in range(len(nums)):
            v1 = nums[i]
            v2 = max_end * nums[i]
            v3 = min_end * nums[i]

            max_end = max(v1, max(v2, v3))
            min_end = min(v1, min(v2, v3))

            res = max(res, max(max_end, min_end))

        return res