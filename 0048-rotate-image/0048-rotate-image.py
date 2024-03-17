class Solution(object):
    def rotate(self, matrix):
        l=len(matrix)
        for i in range(l):
            for j in range(i,l):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #print(matrix)        
        for i in range(l):
            for j in range(0,l//2):
                matrix[i][j],matrix[i][-1-j]=matrix[i][-1-j],matrix[i][j]
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        