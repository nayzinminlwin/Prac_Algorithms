def Is_Palindrome(inputString):

    if len(inputString)<=1 or inputString == None:
        return True
    
    leftIndex = 0
    rightIndex = len(inputString)-1

    while leftIndex<rightIndex:
        
        while leftIndex<rightIndex and not inputString[leftIndex].isalnum():
            leftIndex +=1

        while leftIndex<rightIndex and not inputString[rightIndex].isalnum():
            rightIndex -=1

        if inputString[leftIndex].lower() != inputString[rightIndex].lower():
            return False
        
        leftIndex+=1
        rightIndex-=1

    return True

aString = str(input("Enter a string : "))
print(f"{aString} is Palindrome ? : {Is_Palindrome(aString)}")
print(f"{aString} is Palindrome.") if Is_Palindrome(aString) else print(f"{aString} is not a Palindrome.")