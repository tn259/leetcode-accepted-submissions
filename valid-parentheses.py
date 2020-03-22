class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c == ')' and stack:
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif c == ']' and stack:
                if stack[-1] != '[':
                    return False
                stack.pop()
            elif c == '}' and stack:
                if stack[-1] != '{':
                    return False
                stack.pop()
            else:
                return False
           
        if not stack: return True
        
        return False
      
                
            
            
                
