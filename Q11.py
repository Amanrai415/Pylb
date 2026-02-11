11.class Solution:
    def findMinDiff(self, arr, M):
        n = len(arr)
        
        if M == 0 or M > n:
            return 0
        
        arr.sort()
        
        min_diff = float('inf')
        
        for i in range(n - M + 1):
            min_diff = min(min_diff, arr[i + M - 1] - arr[i])
        
        return min_diff
