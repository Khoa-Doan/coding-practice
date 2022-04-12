class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sCountUp = [0 for _ in range(26)]
        sCountDown = [0 for _ in range(26)]
        tCountUp = [0 for _ in range(26)]
        tCountDown = [0 for _ in range(26)]
        
        for c in t:
            if c.isupper():
                tCountUp[ord(c) - ord('A')] += 1
            else:
                tCountDown[ord(c) - ord('a')] += 1
        
        ans = ""
        l = 0
        for r in range(len(s)):
            if s[r].isupper():
                sCountUp[ord(s[r]) - ord('A')] += 1
            else:
                sCountDown[ord(s[r]) - ord('a')] += 1
            
            while self.isIncluded(sCountUp, sCountDown, tCountUp, tCountDown):
                subS = s[l:r+1]
                if ans == "" or len(ans) > len(subS):
                    ans = subS
                
                if s[l].isupper():
                    sCountUp[ord(s[l]) - ord('A')] -= 1
                else:
                    sCountDown[ord(s[l]) - ord('a')] -= 1
                l += 1
                
        return ans
        
    def isIncluded(self, sCountUp, sCountDown, tCountUp, tCountDown):
        for i in range(26):
            if sCountUp[i] < tCountUp[i] or sCountDown[i] < tCountDown[i]:
                return False
        return True
        