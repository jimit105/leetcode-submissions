class Solution:
    def myAtoi(self, s: str) -> int:
        sign, result = 1, 0
        s = s.lstrip()
        
        idx = 0
        
        if len(s) == 0:
            return 0
        
        if s[0] == '-':
            sign = -1
            idx += 1
            
        elif s[0] == '+':
            idx += 1
            
        int_s = ''
        for i in range(idx, len(s)):
            if s[i].isdigit():
                int_s += s[i]
            else:
                break
                
        int_s = int_s if len(int_s) else "0"
        
        output = int(int_s) * sign
        
        if output < -1 * pow(2, 31):
            return -1 * pow(2, 31)
        
        if output > pow(2, 31) - 1:
            return pow(2, 31) -1
        
        return output
        
        
        
