class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        steps = [0 for i in range(n+1)]
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n+1):
            steps[i] = steps[i-2] + steps[i-1]
        return steps[n]