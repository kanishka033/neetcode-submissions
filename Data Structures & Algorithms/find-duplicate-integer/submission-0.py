class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]

        # step 1: find a meeting point inside the cycle
        for _ in range(len(nums)):
            slow = nums[slow]
            fast = nums[nums[fast]] # keep ahead 

            if slow == fast:
                break
        
        if slow != fast:    # if not a cycle (no duplicate)
            return -1 

        # step 2: find the start to the cycle (the duplicate)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast] 

        return slow      