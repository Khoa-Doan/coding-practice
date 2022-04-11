class Solution:
    def trap(self, height: List[int]) -> int:
        # Calculate the area of the whole thing, then subtract the black area
        """
        totalArea = 0
        l = 0
        r = len(height) - 1
        curMin = 0
        
        while l < r:
            if height[l] > curMin and height[r] > curMin:
                totalArea += (min(height[l], height[r]) - curMin) * (r - l + 1)
                curMin = min(height[l], height[r])
            while height[l] <= curMin and l < r:
                l += 1
            while height[r] <= curMin and l < r:
                r -= 1
        if l == r and height[l] == max(height):
            totalArea += (height[l] - curMin)
        return totalArea - sum(height)
        """
        
        # Dynamic programming with 2 extra arrays
        """
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        ans = 0
        
        for i in range(1, len(left_max)):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(right_max) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        for i in range(0, len(left_max) - 1):
            ans  += min(left_max[i], right_max[i]) - height[i]
        return ans
        """
        
        # Two pointers
        if not height:
            return 0
        leftMax = 0
        rightMax = 0
        l, r = 0, len(height) - 1
        ans = 0
        
        while l < r:
            if height[l] > leftMax:
                leftMax = height[l]
            if height[r] > rightMax:
                rightMax = height[r]
            if leftMax < rightMax:
                ans += max(0, leftMax - height[l])
                l += 1
            else:
                ans += max(0, rightMax - height[r])
                r -= 1
        return ans
                
        