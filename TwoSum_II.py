from typing import List


class Solution(object):
    def TwoSumII(self,nums:List[int],target:int)->List[int]:
        numMap = {}
        for i in range(len(nums)):
            if target-nums[i] in numMap:
                return [numMap[target-nums[i]]+1,i+1]
                pass
            else:
                numMap[nums[i]]= i

        # for i in range(len(nums)):
        #     if target-nums[i] in nums[:i]+nums[i+1:]:
        #         return [i+1,list(nums[:i]+nums[i+1:]).index(target-nums[i])+2]


sol = Solution()
print("HashMap method.")
print(sol.TwoSumII([1,2,3,4],3))
print(sol.TwoSumII([2,7,11,15],22))
print(sol.TwoSumII([2,3,4],6))
print(sol.TwoSumII([-1,0],-1))
print(sol.TwoSumII([0,0,3,4],0))
