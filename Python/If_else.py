
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

m=n%2
print ("remider is : ",m)

if m == 0 :
  print ("the number is even")
  print("vlaue of n ",n)
else : 
  print ("the number is odd")

if n <= 5 and n >= 2 :
  print(n)
  print(m)
  print ("The code worked this far ")
if n>=6 and n<=20 :
    print("the number is between these")
if n>=20 and m==0 :
    print("this is the last condition")
else : 
  print("This is first else")