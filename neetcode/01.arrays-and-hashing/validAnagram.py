class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        hashMap = {}
        for i, c in enumerate(s):
            if c in hashMap:
                hashMap[c] += 1
            else:
                hashMap[c] = 1
                
        for i, c in enumerate(t):
            if c in hashMap:
                hashMap[c] -= 1
            else:
                return False
            
        for key in hashMap:
            if hashMap[key] > 0:
                return False
        
        return True
        
        """
        
        # Solution from NeetCode
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True