def extended_euclidean(a, b):
  if b == 0:
    gcd, s, t = a, 1, 0
    return (gcd, s, t)
  else:
    s2, t2, s1, t1 = 1, 0, 0, 1
    while b > 0:
      q= a // b
      r, s, t = (a - b * q),(s2 - q * s1),( t2 - q * t1)
      a,b,s2,t2,s1,t1=b,r,s1,t1,s,t
    # bezout’s identity
    gcd,s,t=a,s2,t2
    
    return (gcd,s,t)
#Take input
print("Input two non-negative integers a and b such that a>=b")
a, b = map(int, input().split())
x, y = a, b  # Store temporarily
result=extended_euclidean(a,b)
#Print the result
print(f"gcd({x},{y})={result[0]}")
print(f"Linear combination gcd(a,b)=sa+tb:\n {result[0]}={result[1]}*{x}+{result[2]}*{y}")
import turtle
turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

#A= (b**2+c**2-a**2)/(a*b*c)

def triangle(a,b,c,A,B,C):
    
    turtle.fd(a)
    turtle.left(C)
    turtle.fd(b)
    turtle.left(A)
    turtle.fd(c)
    turtle.left(B)

triangle(500,600,700,135.58,122.88,101.54)