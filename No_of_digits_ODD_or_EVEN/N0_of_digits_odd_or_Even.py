
def No_digits_odd_or_even(N):
    count_Even=0
    count_Odd=0
  
    while(N>0):
        a=N%10
        if(a%2==0):
            count_Even+=1
        else:
            count_Odd+=1
        N=N//10
    return count_Even,count_Odd
print(No_digits_odd_or_even(123))