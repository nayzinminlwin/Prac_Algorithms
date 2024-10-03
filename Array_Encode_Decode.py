from typing import List

class Solution:

    def Encode(self, sArr:List[str]) -> str:
        encodedRes =""
        for s in sArr:
            encodedStr = ""
            for c in s:
               encodedStr = encodedStr+ str(ord(c)+1) + ' '
            encodedRes = encodedRes+encodedStr+","

        return encodedRes
    
    def Decode(self,s:str)->List[str]:

        currentDeci,currentAlpha,currentWord = "","",""
        OrgArr = []
        for c in s:
            if c != " " and c!= ",":
                currentDeci = currentDeci+c
            elif (c == " "):
                currentAlpha = chr(int(currentDeci)-1)
                currentWord = currentWord + currentAlpha
                currentDeci = ""
            elif(c == ","):
                OrgArr.append(currentWord)
                currentWord = ""
            else:
                # print("Hey there! I am an error! hehe!")
                pass

        return OrgArr
    

sol = Solution()
encodedResult = sol.Encode(["we","say",":","yes"])
print("Decoded result is ", sol.Decode(encodedResult))