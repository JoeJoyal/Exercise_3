#To print first and Last Number same Integer

def is_equal(N):
    flag=True
    for i in range(1,1000+1):
        if(i%N==0):
            flag=False
            break
    return flag
print(is_equal(121))

   