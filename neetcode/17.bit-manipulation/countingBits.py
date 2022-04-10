class Solution:
    # O(nlogn) solution
    """
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(0, len(ans)):
            ans[i] = self.numOfOneBits(i)
        return ans
        
    def numOfOneBits(self, n):
        ans = 0
        while n > 0:
            n = n & (n-1)
            ans += 1
        return ans
    """
        
    # O(n) solution
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        
        if n == 0:
            return ans
        
        ans[1] = 1
        for i in range(0, len(ans)):
            # i // 2 means i >> 1
            # i % 2 for even/odd number
            ans[i] = ans[i // 2] + ans[i % 2]
        return ans