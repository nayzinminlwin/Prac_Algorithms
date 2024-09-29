from collections import Counter
from typing import List


class Solution:
    def TopFrequent(self,nums:List[int], k:int) -> List[int]:
    
        # all in one line
        # return nums if len(nums)<=1 else [key for key,value in Counter(nums).most_common(k)]

        if len(nums)<= 1:
            return nums

        # hash_map = {}
        # for i in nums:
        #     if i in hash_map:
        #         hash_map[i] +=1
        #     else :
        #         hash_map[i] =1
        # print(hash_map)
        hash_map = Counter(nums)

        # final_arr = []
        # for key,value in hash_map.most_common(k):
        #     final_arr.append(key)
        # return final_arr

        # The upper 4 lines of code in 1 line.
        return [key for key,value in hash_map.most_common(k)]

    def myMethod_TopK_frequentElement(self, nums:List[int], k:int)->List[int]:
        if len(nums)<=1:
            return nums
        
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1

        print(hash_map)
        sortedArr = sorted(hash_map.items(),key= lambda item:item[1], reverse=True)
        print("sorted arr is ",sortedArr)

        resultArr = []
        for i in range(k):
            print("element of sorted arr is ",sortedArr[i][1])
            resultArr.append(sortedArr[i][0])

        return resultArr


sol = Solution()
print(sol.myMethod_TopK_frequentElement([1,1,1,1,1,1,1,1,1,2,2,4,4,4,4,4,4],2))
print(sol.myMethod_TopK_frequentElement([1],1))
