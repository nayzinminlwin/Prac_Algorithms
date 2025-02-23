import re

class Solution:
    def backSlashNCount(self,text,val)->str:
        # write code here
        count =0
        newText = ""
        for i in range(len(text)):
            if text[i] == val[0]:
                if text[i-1] == val[1]:
                    count+=1
                    newText += " \n\n"+str(count+1)+"\n"
            else:
                newText += text[i]
        # print(newText)
        return "\n1\n"+newText
    
    def textGroupCount(self,text)->str:
        count = 0

        # text = input("Enter the text : ")
        text = text.replace('\\n','\n')
        print(re.split(r'\n{2,}',text))
        splitText = "@@".join(re.split(r'\n{2,}',text))
       
        # print(splitText)
        newStr = Solution().backSlashNCount(splitText,"@@")
        return newStr
    
    def readFile(self):
        fileName = input("Input the location of the file : ")
        with open(fileName,"r",encoding="utf-8") as file:
            text = file.read()
            # print(text)
            return text
    def writeFile(self,text):
        fileName = input("Input the location of the file : ")
        with open(fileName,"w",encoding="utf-8") as file:
            text0 = file.write(text)
            return text0

sol = Solution()
newString = sol.textGroupCount(sol.readFile())
print(f"The new String is : {newString}")
sol.writeFile(newString)