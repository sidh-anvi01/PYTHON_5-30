


# a=10 

# b=a*a 
# print(b)
# c=a/a 
# print(c)
# d=a+b 
# print(d)

# e=d-c 
# print(e)

# f=e-c 
# print(f )





# function with return value :

# def add(a,b):
#     total=a+b 
#     return total 

# result=add(32,54)

# print(result)







def resultTenth(c,p,m,h,e):
    total =c+p+m+e+h 
    print(total)
    pers=total/5 
    print(pers)
    if pers>=60:
        return "you are pass "
    else: 
       return "you are fail"



result=resultTenth(45,56,98,78,67)
print(result)