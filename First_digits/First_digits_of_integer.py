# To get the first digits of integer
def first_digits(N):
    sum1=0
    while(N>0):
        rem = N%10
        sum1 = rem
        N = N//10
    return sum1
N=input("Enter the value :")
print(first_digits(N))