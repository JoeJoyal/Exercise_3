#To print count Number of digits
def countdigits(N):
    count=0
    while(N>0):
        N=N//10
        count+=1 
    return count
print(countdigits(123456))