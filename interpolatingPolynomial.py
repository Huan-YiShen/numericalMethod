import numpy as np
import matplotlib.pyplot as plt
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

def add_line_to_plot(plt, p1, p2, startPoint, endPoint):
    a = (p2.y-p1.y)/(p2.x-p1.x)
    b = p2.y - a*p2.x

    x = [startPoint, endPoint]
    y = [a*startPoint+b, a*endPoint+b]
    
    plt.plot(x, y, color='blue', label='linear')


def linear_interpolation(p1, p2, x, soln = 2):
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
    
    if soln == 1:
        term1 = (y2-y1)/(x2-x1)*x
        term2 = (y1*x2 - y2*x1)/(x2-x1)
    else:
        delta = (x-(x1+x2)/2)/h
        term1 = (y2-y1)*delta
        term2 = (y1+y2)/2
    
    return (term1 + term2)

def linear_interpolation_iteration_example(plt, x_start, x_end, interpolating_interval, iteration):
    # Naming the x-axis, y-axis and the whole graph
    plt.title("Linear Interpolation")
    plt.xlabel("input")
    plt.ylabel("output")
    # plt.legend()

    # getting 2 points for interpolation
    iteration = iteration
    interval = (int(x_start)+1 + int(x_end)-1)/iteration
    for i in range(iteration):
        # setting 2 points for interpolation
        ax = 0 + interval*i
        bx = interpolating_interval + interval*i
        ay = np.sin(ax)
        by = np.sin(bx)
        place_to_estimate = (ax+bx)/2
        p1 = Point(ax, ay)
        p2 = Point(bx, by)

        # perform interpolation to determine new points
        add_line_to_plot(plt, p1, p2, x_start, x_end)
        # plt.plot(ax, ay, marker='o', markerfacecolor='red', markersize=3)
        # plt.plot(bx, by, marker='o', markerfacecolor='red', markersize=3)

        estm_res = linear_interpolation(p1, p2, place_to_estimate, 1);
        estm_res_with_rescaling = linear_interpolation(p1, p2, place_to_estimate);
        plt.plot(place_to_estimate, estm_res_with_rescaling, 
                marker='o', markerfacecolor='blue', markersize=5)
        plt.pause(0.05)

    if (estm_res == -999):
        print("linear interpolation should be used if the estimated point is between give points")
    else:
        print("estimation is {}".format(estm_res))

# ##########################################################
# ##########################################################

# ploying sin function from from 0 to 2pi, between 0.1
x_start = 0
x_end = 2*(np.pi)/2
x = np.arange(x_start, x_end, 0.1)
y = np.sin(x)
plt.plot(x, y, color = 'r', label='sine wave')

linear_interpolation_iteration_example(plt, x_start, x_end, 0.01, 20)
plt.show()
