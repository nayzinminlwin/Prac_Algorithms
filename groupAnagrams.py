from collections import Counter, defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        finalArr = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')]+=1

            finalArr[tuple(count)].append(s)

        return list(finalArr.values())


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat","ggwp"]))