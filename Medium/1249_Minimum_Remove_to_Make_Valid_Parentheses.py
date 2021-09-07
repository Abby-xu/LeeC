class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack_par = []
        stack_index = []
        for i in range(len(s)):
            if s[i].islower() != True:
                if len(stack_par) == 0 and len(stack_index) == 0:
                    stack_par.append(s[i])
                    stack_index.append(i)
                else:
                    if stack_par[-1] == '(' and s[i] == ')':
                        stack_par.pop()
                        stack_index.pop()
                    elif stack_par[-1] == ')' or s[i] == '(':
                        stack_par.append(s[i])
                        stack_index.append(i)
        s = list(s)
        while stack_index != []:
            s.pop(stack_index[-1])
            stack_index.pop()
        
        return ''.join(s)
                        
