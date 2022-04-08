class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Brute force
        """
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        
        # Using set
        st = set()
        for i in range(0, len(nums)):
            if nums[i] in st:
                return True
            else:
                st.add(nums[i])
        return False