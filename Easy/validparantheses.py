class Solution:
    def isValid(self, s: str) -> bool:
        openset=['(','{','[']
        closeset=[')','}',']']
        stack=[]
        if len(s)==0:
            return False
        for i in s:
            if i in openset:
                stack.append(i)
            elif i in closeset and len(stack)==0:
                return False
            elif i in closeset and len(stack)>0:
                popped=stack.pop()
                if popped=='(' and i !=')':
                    return False
                elif popped=='{' and i !='}':
                    return False
                elif popped=='[' and i !=']':
                    return False
        if len(stack)>0:
            return False
        return True
        