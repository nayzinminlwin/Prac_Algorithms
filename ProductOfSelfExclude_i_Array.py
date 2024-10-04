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
    
    # Left and Right Array method
    def selfExcludeProduct_0(self, arr:List[int])-> List[int]:
        n = len(arr)
        left_arr = [1]*n
        right_arr = [1]*n
        result_arr = [1]*n
        print("Array is : ",arr)
        print("reserved arr is :",result_arr)
        for i in range(1,n):
            print("i: ",i)
            left_arr[i] = left_arr[i-1] * arr[i-1]
            print(f"Multiply {left_arr[i-1]} and {arr[i-1]},Getting {left_arr}")

        for j in range(n-2,-1,-1):
            print("j: ",j)
            right_arr[j] = right_arr[j+1] * arr[j+1]
            print(f"Multiply {right_arr[i-1]} and {arr[i-1]},Getting {right_arr}")

        for k in range(n):
            result_arr[k] = left_arr[k] * right_arr[k]

        return result_arr
    
sol = Solution()    
# print(sol.selfExcludeProduct_0([-1,0,1,2,3]))
# print(sol.selfExcludeProduct([-1,1,0,-3,3]))
# print(sol.selfExcludeProduct([1,2,3,4]))
# print(sol.selfExcludeProduct([0,0]))
# print(sol.selfExcludeProduct([0,4,0]))

print(sol.selfExcludeProduct_0([1,2,3,4]))