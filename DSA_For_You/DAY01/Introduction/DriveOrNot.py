def drivaOrNot(n):
    if(n<18):
        print("Person can't drive because he is ",n,"(Minor) Years Old")
    elif(n>=18 and n<=65):
         print("Person can drive because he is ",n,"(Adult) Years Old")
    else:
         print("Person can't drive because he is ",n,"(Sr.Citezen) Years Old")

drivaOrNot(17)
drivaOrNot(30)
drivaOrNot(83)