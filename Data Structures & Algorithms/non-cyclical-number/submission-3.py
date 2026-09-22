class Solution:
    def isHappy(self, n: int) -> bool:
        
        # helper function
        def sumOfSquares(n: int) -> int:
            sum = 0
            while n != 0:  # 9 // 10 = 0
                last_digit = n % 10     # remainder
                n = n // 10
                sum = sum + last_digit ** 2
            return sum


        # detect cycle   
        slow = n
        fast = sumOfSquares(n)

        while slow != 1:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
            print(f"slow: {slow} fast: {fast}")

            if slow == 1:
                return True
            if slow == fast:
                return False
        
        return True