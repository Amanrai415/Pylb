17.class Solution:
    def spirallyTraverse(self, mat):
        if not mat: 
            return []
        
        res, n, m = [], len(mat), len(mat[0])
        top, bottom, left, right = 0, n-1, 0, m-1
        
        while top <= bottom and left <= right:
            res += mat[top][left:right+1]; top += 1
            res += [mat[i][right] for i in range(top, bottom+1)]; right -= 1
            if top <= bottom: res += mat[bottom][left:right+1][::-1]; bottom -= 1
            if left <= right: res += [mat[i][left] for i in range(bottom, top-1, -1)]; left += 1
        
        return res
