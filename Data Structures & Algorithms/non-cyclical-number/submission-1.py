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


        freq = {}

        while n != 1:
            n = sumOfSquares(n)
            freq[n] = freq.get(n, 0) + 1

            if freq[n] > 1:
                break

        return True if n == 1 else False