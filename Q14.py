.class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Count elements <= k
        count = sum(1 for num in arr if num <= k)
        
        # Count bad elements in first window
        bad = sum(1 for i in range(count) if arr[i] > k)
        min_swaps = bad
        
        # Sliding window
        for i in range(count, n):
            if arr[i - count] > k:
                bad -= 1
            if arr[i] > k:
                bad += 1
            min_swaps = min(min_swaps, bad)
        
        return min_swaps
