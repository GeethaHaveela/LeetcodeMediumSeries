class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def func(start,path,total):
            if total==target:
                res.append(path[:])  
                return
            if total>target:
                return            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                func(i,path,total+candidates[i])  
                path.pop()  
        func(0,[],0)
        return res
s1 = Solution()
s1.combinationSum([2,3,6,7], 7)