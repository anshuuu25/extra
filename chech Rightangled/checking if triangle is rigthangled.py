#python program to check if a triangle is right angled
import math
# coordinate of the vertices of a triangle
x1 = 1; x2 = -3; x3 = -4
y1 = -3/2; y2 = -7/2; y3 = -3/2
a = math.sqrt(5); b = 5; c = math.sqrt(20);

# now verifying pythagoras

if max(a,b,c)**2 == a**2 + b**2 + c**2 -max(a,b,c)**2 :

  print ("TRUE")

else :
 
  print ("false")
