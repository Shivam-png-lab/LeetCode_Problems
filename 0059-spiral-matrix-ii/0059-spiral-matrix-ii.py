class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top=0
        bottom=n-1
        left=0
        right=n-1
        ecp=1
        matrix = [[0]*n for _ in range(n)]  

        while top<=bottom and left<=right:
        
            for i in range(left,right+1):
                matrix[top][i]=ecp
                ecp+=1
            top+=1
           
            for i in range(top, bottom+1):
                matrix[i][right]=ecp
                ecp+=1
            right-=1
           
            for i in range(right, left-1,-1):
                matrix[bottom][i]=ecp
                ecp+=1
            bottom-=1

          
            for i in range(bottom, top-1,-1):
                matrix[i][left]=ecp
                ecp+=1
            left+=1

        return  matrix