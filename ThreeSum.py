from typing import List

from TwoSum import Solution0


class Solution(object):
    def ThreeIntegerSum(self, nums:List[int])->List[List[int]]:
        if not 3<=len(nums)<=3000:
            return None
        
        nums.sort()
        intArr = set()
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                print("Gotta Continue!")
                continue

            target = 0 - nums[i]
            numArr = nums[:i]+nums[i+1:]

            solution = Solution0()
            tsIndexes =solution.twoSum(numArr,target)

            if tsIndexes:
                triplet = [nums[i],numArr[tsIndexes[0]],numArr[tsIndexes[1]]]
                triplet.sort()
                intArr.add(tuple(triplet))

        return [list(triplets) for triplets in intArr]
    
sol = Solution()
# print(sol.ThreeIntegerSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
print(sol.ThreeIntegerSum([0,1,1])) #[]
# print(sol.ThreeIntegerSum([0,0,0])) #[0,0,0]