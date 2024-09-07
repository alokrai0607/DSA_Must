def isLowerOrUpper(ch:str):
    if(ch.islower()):
        return (ch,"Is in Lower Case")
    else:
        return (ch,"Is in Upper Case")
    
print(isLowerOrUpper("a"))
print(isLowerOrUpper("A"))