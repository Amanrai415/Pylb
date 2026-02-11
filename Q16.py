16.class Solution:
    def findMedian(self, arr):
        arr.sort()
        n = len(arr)
        mid = n // 2
        
        if n % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]
