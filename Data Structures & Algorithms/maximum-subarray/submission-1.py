class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            v1 = nums[i] 
            v2 = curr_sum + nums[i]  # subarray

            curr_sum = max(v1, v2)

            max_sum = max(curr_sum, max_sum)

        return max_sum