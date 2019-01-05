#count the digits using log10
import math
def countdigits(N):
    count =round(math.log(N,10)+1)
    return count
print countdigits(1234)