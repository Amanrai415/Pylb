4.class Solution:    
    def findUnion(self, a, b):
        # Use a set to store distinct elements
        union_set = set()
        
        for x in a:
            union_set.add(x)
            
        for x in b:
            union_set.add(x)
            
        return list(union_set)
