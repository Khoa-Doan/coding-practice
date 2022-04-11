class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1 
        
        counts = [[] for _ in range(len(nums) + 1)]
        for key, value in hashMap.items():
            counts[value].append(key)
            
        ans = []
        for i in range(len(counts) - 1, 0, -1):
            for n in counts[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans