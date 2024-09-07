def isLowerOrUpper(ch:str):
    if(ch.islower()):
        return (ch,"Is in Lower Case")
    else:
        return (ch,"Is in Upper Case")
    
print(isLowerOrUpper("a"))
print(isLowerOrUpper("A"))

#2 nd Way
def isLowerOrUpper(ch:str):
    if(ch>="a" and ch<="z"):
        return (ch,"Is in Lower Case")
    elif(ch>="A" and ch<="Z"):
        return (ch,"Is in Upper Case")
    
print(isLowerOrUpper("a"))
print(isLowerOrUpper("A"))