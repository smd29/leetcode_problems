class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(S)):
            for j in range(len(J)):
                if(S[i]==J[j]):
                    count+=1
        return count