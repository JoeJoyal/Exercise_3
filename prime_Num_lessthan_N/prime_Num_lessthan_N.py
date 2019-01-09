#To Print the prime number from less than N.

def primeNumber_N(N):
    flag =True
    for i in range(2,N):
        if(N%i==0):
            flag =False
            break
    return flag

def is_prime(N):
    sum1=0
    #count =0
    if(N>=1):
        #count+=1
        for i in range(2,N):
            if(primeNumber_N(i)):
                #count+=1
                sum1+=i
        return sum1

#N=input('Enter the value :')
#print(primeNumber_N(N))
print(is_prime(10))   
