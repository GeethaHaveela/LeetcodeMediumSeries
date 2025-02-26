class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1  
        if n<0:
            x=1/x  
            n=-n
        result=1
        while n>0:
            if n%2==1: 
                result=result*x
            x=x*x 
            n//=2  
        return result
s1=Solution()
print(s1.myPow(2.00000,10))