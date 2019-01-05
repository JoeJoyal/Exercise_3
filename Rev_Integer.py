#Reverse given integer N
def RevInteger(N):
    #N=1234
    revnum=0
    while(N>0):
        temp =N%10
        revnum = revnum*10+temp
        N=N//10
    return revnum
print(RevInteger(1234))