class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        ans = 0
        while n > 0:
            ans += (n & 1)
            n >>= 1
        return ans
        """
    
        # Trick answer
        ans = 0
        while n > 0:
            n = n & (n-1)
            ans += 1
        return ans