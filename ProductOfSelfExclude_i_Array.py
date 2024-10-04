from typing import List

class Solution:
    # Division Operation O(n)
    def selfExcludeProduct(self, nums:List[int])->List[int]:
        productArr = [0]*len(nums)
        res =1 

        if nums.count(0) == len(nums):
            return nums
        elif nums.count(0)>1:
            return productArr
        
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            res = res * nums[i]
        # print(res)

        if 0 in nums:
            for k in range(len(nums)):
                if nums[k] == 0:
                    productArr[k] = res
        else: 
            for j in range(len(productArr)):
                productArr[j] = int(res/nums[j])
        return productArr
    
sol = Solution()    
print(sol.selfExcludeProduct([-1,0,1,2,3]))
print(sol.selfExcludeProduct([-1,1,0,-3,3]))
print(sol.selfExcludeProduct([1,2,3,4]))
print(sol.selfExcludeProduct([0,0]))
print(sol.selfExcludeProduct([0,4,0]))