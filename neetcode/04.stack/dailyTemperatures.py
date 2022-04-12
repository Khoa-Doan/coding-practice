class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        
        stack = [(temperatures[0], 0)] # pair: temp, index
        ans = [0 for _ in range(len(temperatures))]
        
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, day = stack.pop()
                ans[day] = i - day
            stack.append((temperatures[i], i))

        return ans