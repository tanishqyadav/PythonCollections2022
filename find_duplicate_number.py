class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l={}
        for i in nums:
            
            if i not in l:
                l[i]=1
            else:
                l[i]+=1
                
        for i,j in l.items():
            if j>1:
                return i
              
# input will be a list
#this will return the duplicate number
