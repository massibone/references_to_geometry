from math import sqrt
from turtle import color, begin_fill, forward, left, end_fill, done
from math import acos, degrees

print('Pythagorean theorem')

formula = input('For which side do you wish to calculate hypotenuse?a,b or c ')

if formula == 'c':
	side_a = int(input('Input the length of side a: '))
	side_b = int(input('Input the length of side b: '))

	side_c = sqrt(side_a * side_a + side_b * side_b)
	
	print('The hypotenuse c is: ', side_c )
	

elif formula == 'a':
    side_b = int(input('Input the length of side b: '))
    side_c = int(input('Input the length of side c: '))
    
    side_a = sqrt((side_c * side_c) - (side_b * side_b))
    
    print('The hypotenuse is ', side_a )
    

elif formula == 'b':
    side_a = int(input('Input the length of side a: '))
    side_b = int(input('Input the length of side c: '))
        
    side_c = sqrt((side_c*side_c) - side_a * side_a)
    
    print('The length of side b is')
    print(side_c)

else:
	print('Please select a side between a, b, c')

def triangle_exists(a, b, c):
    """Return True if there exists a triangle with sides a, b, c."""
    return a + b > c and b + c > a and c + a > b

def triangle_angle(a, b, c):
    
    return degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2.0 * b * c)))

def draw_triangle(a, b, c):
    """Draw a triangle with sides of lengths a, b, and c."""
    assert(triangle_exists(a, b, c))
    color('black', 'blue')
    begin_fill()
    forward(c)
    left(180 - triangle_angle(b, c, a))
    forward(a)
    left(180 - triangle_angle(c, a, b))
    forward(b)
    end_fill()
    done()

draw_triangle(side_a*10,side_b*10, side_c*10)