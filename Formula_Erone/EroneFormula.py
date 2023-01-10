
import math
import string

a = float(input('Insert first side:  '))

b = float(input('Insert second side: '))

c = float(input('Insert third side: '))

print
print
p2= (a+b+c) 
p = (p2)/2
print(p)
A = math.sqrt(p*(p-a)*(p-b)*(p-c))

print (" Erone Formula is =" ,A,"squared cm")

