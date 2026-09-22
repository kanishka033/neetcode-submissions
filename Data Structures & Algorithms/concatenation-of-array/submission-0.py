class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        n = len(nums)

        for i in range(n):
            ans.append(nums[i])

        return ans
