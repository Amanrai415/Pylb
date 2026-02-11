2.class Solution:
    def getMinMax(self, arr):
        if not arr:
            return []
        
        minimum = maximum = arr[0]
        
        for num in arr[1:]:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        
        return [minimum, maximum]
