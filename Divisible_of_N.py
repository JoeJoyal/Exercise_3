#Divisible of given N
def divisible_N(N):
    while(N>0):
        temp = N%10
        if(N%temp==0):
            N =N//10
        else:
            return "Num can't be divided"
    return "Num can be divided by all integer"
print(divisible_N(36))