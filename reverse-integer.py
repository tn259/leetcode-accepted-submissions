class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        negative = False
        neg_limit = -(2**31)
        pos_limit = 2**31 - 1
            
        if x < 0:
            negative = True
            x = -x if x > neg_limit else 0
        else:
            x = x if x < pos_limit else 0
            
        while x > 0:
            output = (output * 10) + (x % 10)
            x = int(x / 10)
        
        if negative:
            output = -output if -output > neg_limit else 0
        else:
            output = output if output < pos_limit else 0
        
        return output
