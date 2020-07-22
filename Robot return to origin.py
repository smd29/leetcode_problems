class Solution:
    def judgeCircle(self, moves: str) -> bool:
        #print(len(moves))
        l_count = r_count = u_count = d_count =0
        for i in range(0,len(moves)):
            if(moves[i]=='L'):
                l_count+=1
            elif(moves[i]=='R'):
                r_count+=1
            elif(moves[i]=='U'):
                u_count+=1
            elif(moves[i]=='D'):
                d_count+=1
        if(l_count==r_count and u_count==d_count):
            return True
        else:
            return False