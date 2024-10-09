from typing import List

from TwoSum import Solution0


class Solution(object):
    def ThreeIntegerSum(self, nums:List[int])->List[List[int]]:
        if not 3<=len(nums)<=3000:
            return None
        
        nums.sort()
        intArr = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            print("numssssssssssssss : ",nums)
            target = 0 - nums[i]
            print("target is :::::::", target)
            numArr = nums[:i]+nums[i+1:]
            print("Num arr is now :::::::", numArr)
            solution = Solution0()
            tsIndexes =solution.twoSum(numArr,target)
            if tsIndexes:
                intArr.append([nums[i],numArr[tsIndexes[0]],numArr[tsIndexes[1]]])

        print(intArr)

        return intArr
    
sol = Solution()
print(sol.ThreeIntegerSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
# print(sol.ThreeIntegerSum([0,1,1])) #[]
# print(sol.ThreeIntegerSum([0,0,0])) #[0,0,0]