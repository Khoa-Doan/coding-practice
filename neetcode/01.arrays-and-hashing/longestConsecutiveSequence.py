class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        ans = 0
        for n in nums:
            # check if its the start of a sequence
            if n-1 in hashSet:
                continue
            curLength = 1
            while n + curLength in hashSet:
                curLength += 1
            ans = max(ans, curLength)
        return ans