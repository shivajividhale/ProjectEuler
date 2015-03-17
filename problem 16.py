__author__ = 'Shivaji'

import math
square_values={0:1,1:2,2:4,3:8,4:16}
def power2(n):
    if n%2==0:
        j=power2(n/2)
        square_values.push()
        return j
    else:
        j=2*math.pow(2,square_values[n-1])
        return

