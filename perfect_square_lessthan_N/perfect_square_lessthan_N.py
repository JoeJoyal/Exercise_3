#To print the sum of perfect square less than N

import math
def perfectSquare(N):
    flag=True
    x = math.sqrt(N)
    m = round(x)
    if(m-x==0):
        flag = False
    return flag

#N=input("Enter the value :")
print(perfectSquare(5))