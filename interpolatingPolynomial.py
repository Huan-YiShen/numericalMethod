import numpy as np
# evaluate interpolating polynomial at a point close to x_k
# extimate the derivative at the point x_k
# estimate an integral from some point x_k-n up to x_k

# x_k = x_0+k*h
# x_(k-1) = x_k-h
# x_(k+1) = x_k+h
# where h is the slope of the linear function used for interpolation
# interpolation is only accurate when estimating point between the known points
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def linear_interpolation(p1, p2, x):
    # interpolates a expression (f or curve) with a line that goes through 2 points on the curve
    # solution 1: using 2 arbitrary points on the curve (x1, f(x1)) and (x2, f(x2)), 
    #   find a line that goes through the 2 points. This is not precise because
    #   linear interpolation only works when points are close  
    # solution 2: find a linear equation a1*d+a0, that goes through (-0.5, f(x1)) and (0.5, f(x2))  
    #   this effectively shifts f(x1) and f(x1) to near the origin and horizontally compress 
    #   the function so xn1 to x have distance of 1, the compression factor is 1/h. 
    #   Due to this transformation, the estimating point (x) also need to be transformed d = (x-(x1+x2)/2)/h
    x1 = p1.x
    x2 = p2.x
    y1 = p1.y
    y2 = p2.y
    if (x1 < x2):
        if x < x1 or x > x2:
            return -999
    else: 
        if x > x1 or x < x2:
            return -999

    h = abs(x2-x1)
    # term1 = (y2-y1)/(x2-x1)*x
    # term2 = (y1*x2 - y2*x1)/(x2-x1)

    delta = (x-(x1+x2)/2)/h
    term1 = (y2-y1)*delta
    term2 = (y1+y2)/2
    
    return (term1 + term2)


ax = 1
ay = 1
bx = 2
by = 2
p1 = Point(ax, ay)
p2 = Point(bx, by)

estm = linear_interpolation(p1, p2, 1.7);

if (estm == -999):
    print("linear interpolation should be used if the estimated point is between give points")
else:
    print("estimation is {}".format(estm));