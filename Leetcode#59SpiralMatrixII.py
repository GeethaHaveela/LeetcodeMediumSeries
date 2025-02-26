class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[]
        for i in range(n):
            row=[0]*n 
            matrix.append(row)
        left,right,top,bottom=0,n-1,0,n-1
        num=1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1          
            for i in range(top,bottom+1):
                matrix[i][right]=num
                num+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=num
                    num+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=num
                    num+=1
                left+=1   
        return matrix
s1=Solution()
print(s1.generateMatrix(3))