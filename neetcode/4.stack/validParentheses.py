class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack = []
        # Make a set of left parentheses
        lefts = { '(', '{', '['}
        
        for c in s:
            if c in lefts:
                stack.append(c)
            elif c not in lefts and not stack:
                return False
            elif (c == ')' and stack[-1] == '(') \
                    or (c == '}' and stack[-1] == '{') \
                    or (c == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
        
        # Edge case: there are still leftover open parentheses
        if stack:
            return False
            
        return True
        """
    
        # Cleaner solution using map
        hashMap = {'(': ')', '{':'}', '[':']'}
        stack = []
        
        for c in s:
            if c in hashMap:
                stack.append(c)
                continue
            if not stack or c != hashMap[stack[-1]]:
                return False
            stack.pop()
            
        return not stack