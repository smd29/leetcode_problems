class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if(x<0):
            return False
        else:
            while(x>0):
                rem=x%10
                rev=rev*10+rem
                # print(rev)
                x=x//10
            # print(rev)
            if(rev==temp):
                return True
            else:
                return False