class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans=nums[0]+nums[1]+nums[2]
        nums.sort()
        diff=abs(ans-target)
        for i in range(len(nums)):
            first=nums[i]
            start=i+1
            end=len(nums)-1
            while(start<end):
                if(first+nums[start]+nums[end]==target):
                    return target
                elif(abs(first+nums[start]+nums[end]-target))<diff:
                    diff=abs(first+nums[start]+nums[end]-target)
                    ans=first+nums[start]+nums[end]
                if(first+nums[start]+nums[end]>target):
                    end=end-1
                else:
                    start=start+1
        return ans
s1=Solution()
print(s1.threeSumClosest([-1,2,1,-4],1))