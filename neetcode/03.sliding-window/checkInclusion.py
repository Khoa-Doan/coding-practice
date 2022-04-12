class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS1 = [0 for _ in range(26)]
        countS2 = [0 for _ in range(26)]
        
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            matches = matches + 1 if countS1[i] == countS2[i] else matches

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # handle adding character
            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS2[index] == countS1[index]:
                matches += 1
            elif countS2[index] - 1 == countS1[index]:
                matches -= 1
                
            # handle removing character
            index = ord(s2[l]) - ord('a')
            countS2[index] -= 1
            if countS2[index] == countS1[index]:
                matches += 1
            elif countS2[index] + 1 == countS1[index]:
                matches -= 1
            l += 1
            
            
        return matches == 26
        