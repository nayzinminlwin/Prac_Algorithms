class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # # My method : O(n^2)

        # # for i in numms:
        # #     if target-i in nums:
        # #         return [i,target-i]
        # for i in range(len(nums)):
        #     new_arr = nums[:i]+nums[i+1:]
        #     print(i,nums)
        #     if target-nums[i] in new_arr:
        #         return [i,new_arr.index(target-nums[i])+1]
            
        # return None
    
        # AI Method : Using a Single Loop with a Lookup Table (Dictionary) : O(n)
        lookup = {}
        print(lookup)
        print("array is ", nums,"target is", target)

        for j, num in enumerate(nums):
            print("j and num is now : ",j,num)

            complement  = target - num
            print("Compliment is now :",complement)
            if complement in lookup:
                print("Found at : ",j, "lookup val is",lookup[complement])
                return [lookup[complement],j]
            lookup[num]=j

            print("updated lookup is ",lookup)

        return None

    
sol = Solution()
print(sol.twoSum([5,3,1,3,3,33,3,1],2))
        