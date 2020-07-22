class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        if n ==0 or n==1:
            return 1
        elif n==2:
            return 2
        else:
            res[0] = 1
            res[1] = 1
            res[2] = 2
      
            for i in range(3, n + 1) : 
                res[i] = res[i - 1] + res[i - 2]  
        #print(res)
            return res[n]        