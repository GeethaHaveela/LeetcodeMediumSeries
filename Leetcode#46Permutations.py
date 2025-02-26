class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(path,available):
            if not available:
                result.append(path)
                return 
            for i in range(len(available)):
                backtrack(path+[available[i]],available[:i] +available[i+1:])    
        backtrack([],nums)
        return result
s1=Solution()
print(s1.permute([1,2,3]))