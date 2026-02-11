5.class Solution:
    def largest(self, arr):
        if not arr:
            return None  # or raise an exception if array is empty
        
        maximum = arr[0]
        for num in arr[1:]:
            if num > maximum:
                maximum = num
        return maximum
