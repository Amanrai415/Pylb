10.class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 0 or arr[0] == 0:
            return -1
        
        jumps = 0
        maxReach = arr[0]
        step = arr[0]
        
        for i in range(1, n):
            if i == n - 1:
                return jumps + 1
            
            maxReach = max(maxReach, i + arr[i])
            step -= 1
            
            if step == 0:
                jumps += 1
                if i >= maxReach:
                    return -1
                step = maxReach - i
        
        return -1
