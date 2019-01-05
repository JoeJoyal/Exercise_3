def panlindrom(N):
    temp=0
    count_even =0
    count_odd =0
    while(N>0):
        rem = N%10
        temp=temp*10+rem
        N=N//10

        if(rem%2==0):
            count_even+=1
        else:
            count_odd+=1
    return count_even,count_odd
print(panlindrom(1234))
