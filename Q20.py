20.class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        
        max_row_index = -1
        j = m - 1  # Start from top-right corner
        
        for i in range(n):
            # Move left while there are 1s
            while j >= 0 and arr[i][j] == 1:
                j -= 1
                max_row_index = i  # Update row index
        
        return max_row_index
