class Solution:
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        self.generateParenthesisHelper(stack, ans, n, n)
        return ans
    
    def generateParenthesisHelper(self, stack, ans, nOpen, nClose):
        if nOpen == 0 and nClose == 0:
            ans.append(''.join(stack))
            return
        if nOpen >= 1 and nOpen <= nClose:
            stack.append('(')
            self.generateParenthesisHelper(stack, ans, nOpen - 1, nClose)
            stack.pop()
        if nClose >= 1 and nClose >= nOpen:
            stack.append(')')
            self.generateParenthesisHelper(stack, ans, nOpen, nClose - 1)
            stack.pop()
    """
    
    # Backtracking
    def generateParenthesis(self, n: int) -> List[str]:  
        stack = []
        ans = []
        
        def backtrack(nOpen, nClose):
            if nOpen == n and nClose == n:
                ans.append(''.join(stack))
                
            if nOpen < n:
                stack.append('(')
                backtrack(nOpen + 1, nClose)
                stack.pop()
                
            if nClose < nOpen:
                stack.append(')')
                backtrack(nOpen, nClose + 1)
                stack.pop()
        
        backtrack(0, 0)
        return ans