from typing import List

class Solution(object):
    # My Solution
    def Longest_Consecutive(self,nums:List[int])->int:
        if nums == [] or nums == None:
            return 0
        length = 1
        longestLen = 1
        nums = sorted(nums)
        print("Sorted arr is now : ", nums)
        for i in range(len(nums)-1):
            # print("i and i+1 :",nums[i],nums[i+1])
            # print("i+1 and [i]+1 :",nums[i]+1,nums[i+1])
            if nums[i] == nums[i+1]:
                # print("Gotta Continue")
                continue
            elif nums[i]+1 == nums[i+1]:
                length+=1
                # print("Adding +1 to len,now len is : ", length)
                
            else:
                # print("Validating length")
                if length>longestLen:
                    longestLen = length
                length = 1
            # print("Len:",length, "Long len:", longestLen)
        if length>longestLen:
            longestLen = length
        return longestLen
    
    # My Solution, But Compact Version
    def Longest_ConsecutiveSequence_CompactVer(self, numArr:List[int])->int:
        if not numArr:
            return 0
        numArr = sorted(set(numArr))
        Length = 1
        longLength = 1
        for i in range(len(numArr)-1):
            if numArr[i]+1 == numArr[i+1]:
                Length+=1
            else:
                longLength = max(Length,longLength)
                Length =1
        
        return max(Length,longLength)
    
sol = Solution()
print("Length : ",sol.Longest_ConsecutiveSequence_CompactVer([4,8,1,1,10,7,2,6]))
print("Length : ",sol.Longest_Consecutive([4,8,1,1,10,7,2,6]))
print("Length : ",sol.Longest_ConsecutiveSequence_CompactVer([0,3,7,2,5,8,4,6,0,1]))
print("Length : ",sol.Longest_ConsecutiveSequence_CompactVer([2,20,4,10,3,4,5]))
print("Length : ",sol.Longest_ConsecutiveSequence_CompactVer([0,3,2,5,4,6,1,1]))
print("Length : ",sol.Longest_ConsecutiveSequence_CompactVer([100,4,200,1,3,2]))