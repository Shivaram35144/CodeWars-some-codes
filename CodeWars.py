#Area and perimeter of the ellipse

import math
def ellipse(a,b):
    area = round(math.pi*a*b,1)
    peri=round(math.pi*(1.5*(a+b)-math.sqrt(a*b)),1)
    print("Area: ",area,", perimeter: ",peri)

ellipse(5,2)
