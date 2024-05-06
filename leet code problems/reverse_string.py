class Solution:
    def reverse_String(self,lst):
        left=0
        right= len(lst)-1
        while left <right:
            hold = lst[left]
            lst[left]= lst[right]
            lst[right]= hold
            left+=1
            right-=1
        return lst
l=['h','e','e','l','o']
obj= Solution()
print(obj.reverse_String(l))