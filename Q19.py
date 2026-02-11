19.class Solution:
    def median(self, mat):
        # Flatten the matrix
        flat = [num for row in mat for num in row]
        flat.sort()
        n = len(flat)
        
        # Median is middle element (since n*m is odd)
        return flat[n // 2]
