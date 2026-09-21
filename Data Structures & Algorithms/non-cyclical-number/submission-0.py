class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1:
            if n in seen:
                return False
            seen[n] = True
            n = sum(int(d) ** 2 for d in str(n))
        return True