class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        while matrix:
            result=result+matrix.pop(0)  
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result=result+matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))  
        return result
s1=Solution()
print(s1.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))