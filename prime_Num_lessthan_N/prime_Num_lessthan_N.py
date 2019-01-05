#To Print the prime number from less than N.
def primeNumber_N(N):
    flag =True
    for i in range(2,N):
        if(N%i==0):
            flag =False
            break
    return flag

def is_prime(N):
    count =0
    if(N>=1):
        count+=1
        for i in range(2,N):
            if(primeNumber_N(i)):
                count+=1
        print(count)


#N=input('Enter the value :')
#print(primeNumber_N(5))
print(is_prime(5))   
