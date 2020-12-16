from math import *

class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        else:
            log_val = math.log2(x)
            power_val = 0.5 * log_val
            return math.floor(2 ** power_val)
