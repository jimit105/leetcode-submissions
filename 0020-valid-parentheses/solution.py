class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mappings = {')': '(',
                    ']':'[',
                    '}':'{'}
        
        for char in s:
            
            # check if is it closing bracket
            if char in mappings:
                
                # popping the last opening bracket, closing bracket is never pushed to the stack
                last_element = stack.pop() if stack else '#'
                
                if mappings[char] != last_element:
                    return False
                
                
            # its char in opening bracket, append to stack
            else:
                stack.append(char)
            
            
                
                
        # if still there are elements in the stack, then return False
        return not stack
