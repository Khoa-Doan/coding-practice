class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            tup = tuple(letters)
            if tup in hashMap:
                hashMap[tup].append(s)
            else:
                hashMap[tup] = [s]
        #ans = []
        #for key in hashMap:
        #    ans.append(hashMap[key])
        #return ans
        return hashMap.values()