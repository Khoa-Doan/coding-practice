class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        string = ""
        for i,c in enumerate(s):
            if c.isalnum():
                string += c.lower()
        
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
            
        return True
        """
        
        # In-place
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            
        return True