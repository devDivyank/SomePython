import math
import random
import string
 
def generate_fibbo(lst):
    while lst[-1]+lst[-2] <= 4000000:
        lst.append(lst[-1]+lst[-2])
    return lst

mylist = [1, 2]
fibo_list = generate_fibbo(mylist)
total = 0
for x in fibo_list:
    if x%2==0:
        total += x

print(total)
 
