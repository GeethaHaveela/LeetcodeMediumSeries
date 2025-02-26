class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()  
        used=[False]*len(nums) 

        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])  
                return
            
            for i in range(len(nums)):
                if used[i]:  
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue

                used[i]=True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=False
        
        backtrack([])
        return res
s1=Solution()
print(s1.permuteUnique([1,1,2]))