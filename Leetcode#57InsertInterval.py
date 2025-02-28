class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        i=0
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i=i+1
        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i=i+1
        result.append(newInterval)
        while i<len(intervals):
            result.append(intervals[i])
            i=i+1
        return result
s1=Solution()
print(s1.insert([[1,3],[6,9]],[2,5]))