class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            mask = 1 << i
            bit = n & mask
            ans = ans | (bit >> i << (31 - i))
        return ans