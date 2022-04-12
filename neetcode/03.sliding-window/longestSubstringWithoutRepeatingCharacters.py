class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        st = set()
        ans = 0
        
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[slow])
                slow += 1
            st.add(s[i])
            ans = max(ans, i - slow + 1)
        return ans
    
        
            
        