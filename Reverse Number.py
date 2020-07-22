class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        #print(-123%10)
        
        
        if(x>=0):
            while(x!=0):
                rem = x%10
                rev = rev*10+rem
                x=x//10
            #print(rev)
            if(rev<=(pow(2,31)-1) and rev >= (-pow(2,31))):
                return rev
            else:
                return 0
        else:
            x = 0-x
            while(x!=0):
                rem = x%10
                rev = rev*10+rem
                x=x//10
            if(rev<=(pow(2,31)-1) and rev >= (-pow(2,31))):
                return (0-rev)
            else:
                return 0
            