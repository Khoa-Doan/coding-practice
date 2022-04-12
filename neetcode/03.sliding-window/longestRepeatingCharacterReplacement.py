class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        ans = 0
        
        l = 0   # left pointer
        for r in range(len(s)): # right pointer
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # substring length - number of chars need to be replaced
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
        return ans