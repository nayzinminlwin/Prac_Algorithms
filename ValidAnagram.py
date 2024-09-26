# from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        # s = list(s)
        # t = list(t)

        # method 1 : nested for loop method

        # method 2 : is available in dictionary? method
        # for i in s:
        #     if i in t:
        #         t.remove(i)
        # if len(t)==0:
        #     return True

        # method 3 : built-in Counter function method
        # s_counter = Counter(s)
        # t_counter = Counter(t)
        # # print(s_counter, t_counter)
        # if s_counter == t_counter:
        #     return True
        # else :
        #     return False
        
        # method 4 : sorting and comparing method
        # if sorted(s) == sorted(t):
        #     return True
        # else :
        #     return False
        
        # method 5 : Array Frequency Counting method
        # Creating array size of 26 for a to z 
        count = [0] * 26

        # looping the length
        for i in range(len(s)-1):
            # if see an alpha, it will do +1 or -1 to respective index
            count[ord(s[i])-ord('a')] +=1
            count[ord(t[i])-ord('a')] -=1

        # if every index in array count is neutral,0 : Anagram is true.
        for c in count:
            if c!=0:
                return False
            
        return True
        

sol = Solution()   
print(sol.isAnagram("anagram","nagaram"))