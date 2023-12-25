class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        trim=[]
        for i in s:
            if i.isalpha():
                trim.append(i.upper())
            elif i.isnumeric():
                trim.append(i)
        
        left=0
        right=len(trim)-1
        while left<right:
            if trim[left]!=trim[right]:
                return False
            left+=1
            right-=1
        return True
            
        