class Solution:
    def toLowerCase(self, str: str) -> str:
        output = ""
        for i in range(0,len(str)):
            y= ord(str[i])
            if(y>=65 and y<=90):
                y=y+32
            #x=str(y)
            output=output+chr(y)
        #print('"'+output+'"')
        return (output)