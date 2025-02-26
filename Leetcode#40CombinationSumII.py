class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort() 
        def func(start,path,total):
            if total==target:
                res.append(path[:])  
                return
            if total>target:
                return
            prev=-1  
            for i in range(start,len(candidates)):
                if candidates[i]==prev:  
                    continue  
                path.append(candidates[i])
                func(i+1,path,total+candidates[i]) 
                path.pop()  
                prev = candidates[i] 
        func(0,[],0)
        return res
s1=Solution()
print(s1.combinationSum2([10,1,2,7,6,1,5],8))