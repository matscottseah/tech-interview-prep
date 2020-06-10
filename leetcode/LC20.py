def isValid(self, s: str) -> bool:
    myStack = []
    
    if len(s) % 2 != 0:
        return False
    
    for parentheses in s:
        if parentheses == '(' or parentheses == '{' or parentheses == '[':
            myStack.append(parentheses)
        else:
            if len(myStack) != 0:
                top = myStack.pop()
                if parentheses == ')' and top != '(':
                    return False
                elif parentheses == '}' and top != '{':
                    return False
                elif parentheses == ']' and top != '[':
                    return False
            else:
                return False
            
    if len(myStack) == 0:
        return True
    else:
        return False