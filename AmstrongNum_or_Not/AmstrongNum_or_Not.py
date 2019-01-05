#Amstrong Num or Not
def Amstrong_Num(N):
    sum1=0
    while(N!=0):
        rem =N%10
        sum1 = (rem**3)+sum1
        N = N//10
    return sum1
print(Amstrong_Num(153))