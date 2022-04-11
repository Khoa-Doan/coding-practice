class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Brute force
        """
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans[i] *= nums[j]
        return ans
        """
    
        # O(n) time complexity and O(n) space complexity
        """
        pre = [1 for _ in range(len(nums))]
        for i in range(1, len(pre)):
            pre[i] = pre[i-1] * nums[i-1]
            
        post = [1 for _ in range(len(nums))]
        for i in range(len(post) - 2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
            
        ans = [1 for _ in range(len(nums))]
        for i in range(len(ans)):
            ans[i] = pre[i] * post[i]
        return ans
        """
        
        # O(n) time complexity and O(1) space complexity
        ans = [1 for _ in range(len(nums))]
        
        pre = 1
        for i in range(len(ans)):
            ans[i] = ans[i] * pre
            pre = pre * nums[i]
            
        post = 1
        for i in range(len(ans) - 1, -1, -1):
            ans[i] = ans[i] * post
            post = post * nums[i]
            
        return ans