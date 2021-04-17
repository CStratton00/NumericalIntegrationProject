"""
Collin Stratton
CST-305
Topic 8 Project 8: Numerical Integration
Dr. Ricardo Citro

For this project, this is the coding section for part 1 where we are to graph the integrals of the functions
given throughout part 1 and output their values

Implementation approach:
- Research scipy integrals
- Developed functions for the functions given in the doc
- Created a graphing function to plot the area under the graph
- Plotted the graphs using the created graphing function
- Outputted the integrals of each of the functions
"""

# Packages used: matplotlib, numpy, scipy
from scipy import pi                    # import pi from scipy to use in functions
from scipy.integrate import quad, simps # import quad from scipy integrate function to integrate functions
import numpy as np                      # import numpy as np to use the numpy functions
import matplotlib.pyplot as plt         # import pyplot as plot from matplotlib to plot functions

# function to plot the reimann sum on a function
def reimann_plot(f, minlim, maxlim, N):       # input the function, lowerbound, uppderbound, and the number of iterations
    n = 1000            # number of points to graph, makes it smooth

    x = np.linspace(minlim, maxlim, N + 1)        # x space to graph the bar charts on
    y = f(x)                                      # y space based on the x space and function inputted
    X = np.linspace(minlim, maxlim, n * N + 1)    # x space slightly larger than the bar chart area
    Y = f(X)                                      # y space based on the slightly larger x space and function inputted

    plt.figure(figsize=(15,5))          # create graph space of size 15 by 5

    plt.subplot(1, 3, 1)                # first plot out of 3 in the created graph space
    plt.plot(X, Y, 'b')                 # graph the slightly larger x and y space
    x_left = x[:-1]                     # left endpoints x space
    y_left = y[:-1]                     # left endpoints y space

    # plot the graph with the x and y points that represent the left endpoints and format the colors of the graph
    plt.plot(x_left,y_left, 'b.', markersize = 10)
    plt.bar(x_left, y_left, width = (maxlim - minlim) / N, alpha = 0.2, align = 'edge', edgecolor = 'b')
    plt.title('Left Riemann Sum, N = {}'.format(N))

    plt.subplot(1, 3, 2)                # second plot out of 3 in the created graph space
    plt.plot(X, Y, 'b')                 # graph the slightly larger x and y space
    x_mid = (x[:-1] + x[1:]) / 2        # midpoints x space
    y_mid = f(x_mid)                    # midpoints y space

    # plot the graph with the x and y points that represent the midpoints and format the colors of the graph
    plt.plot(x_mid, y_mid, 'b.', markersize = 10)
    plt.bar(x_mid,y_mid, width = (maxlim - minlim) / N, alpha = 0.2, edgecolor = 'b')
    plt.title('Midpoint Riemann Sum, N = {}'.format(N))

    plt.subplot(1, 3, 3)                # third plot out of 3 in the created graph space
    plt.plot(X, Y, 'b')                 # graph the slightly larger x and y space
    x_right = x[1:]                     # right endpoints x space
    y_right = y[1:]                     # right endpoints y space

    # plot the graph with the x and y points that represent the right endpoints and format the colors of the graph
    plt.plot(x_right, y_right, 'b.', markersize = 10)
    plt.bar(x_right, y_right, width = -(maxlim - minlim) / N, alpha = 0.2, align = 'edge', edgecolor = 'b')
    plt.title('Right Riemann Sum, N = {}'.format(N))

    plt.show()      # show the graph

# function to find the reimann sum for the left, middle, and right hand approximations
def reimann_sum(f, minlim, maxlim, N):      # input the function, lowerbound, upperbound, and the number of iterations
    dx = (maxlim - minlim)/N                                # number of steps to solve
    x_left = np.linspace(minlim, maxlim - dx, N)            # step size for the left hand approximation
    x_midpoint = np.linspace(dx / 2, maxlim - dx / 2, N)    # step size for the midpoint approximation
    x_right = np.linspace(dx, maxlim, N)                    # step size for the right hand approximation

    left_riemann_sum = np.sum(f(x_left) * dx)               # find the left hand sum approximation
    print("Left Riemann Sum:\t", left_riemann_sum)          # print the left hand sum approximation

    midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)       # find the midpoint sum approximation
    print("Midpoint Riemann Sum:\t", midpoint_riemann_sum)  # print the left hand sum approximation

    right_riemann_sum = np.sum(f(x_right) * dx)             # find the right hand sum approximation
    print("Right Riemann Sum:\t", right_riemann_sum)        # print the left hand sum approximation

# functions to integrate
f = lambda x: np.sin(x) + 1                 # Part 1a function writen as a lambda function
g = lambda x: (3 * x) + (2 * (x ** 2))      # Part 1b function writen as a lambda function
h = lambda x: np.log(x)                     # Part 1c1 function writen as a lambda function
i = lambda x: (x ** 2) - (x ** 3)           # Part 1c2 function writen as a lambda function

# print the values of the integrals
print("\nThe riemman sum of the function in Part 1a is:"); reimann_sum(f, -pi, pi, 4)       # find integral of function f using riemann sum
print("The correct value for part 1a is: ", quad(f, -pi, pi)[0])                            # find the correct value of the integral for Part 1a
print("\nThe riemman sum of the function in Part 1b is:"); reimann_sum(g, 0, 1, 1000)       # find integral of function g using riemann sum
print("The correct value for part 1b is: ", quad(g, 0, 1)[0])                               # find the correct value of the integral for Part 1b
print("\nThe riemman sum of the function in Part 1c1 is:"); reimann_sum(h, 1, np.e, 1000)   # find integral of function h using riemann sum
print("The correct value for part 1c1 is: ", quad(h, 1, np.e)[0])                           # find the correct value of the integral for Part 1c1
print("\nThe riemman sum of the function in Part 1c2 is:"); reimann_sum(i, -1, 0, 1000)     # find integral of function i using riemann sum
print("The correct value for part 1c2 is: ", quad(i, -1, 0)[0])                             # find the correct value of the integral for Part 1c2

# plot the graphs of the integrals
reimann_plot(f, -pi, pi, 4)     # graph the f function integral based on the given range
reimann_plot(g, 0, 1, 50)       # graph the g function integral based on the given range
reimann_plot(h, 1, np.e, 50)    # graph the h function integral based on the given range
reimann_plot(i, -1, 0, 50)      # graph the i function integral based on the given range

# Part 2
# creation of the x space and y space based on the data gathered from downloading a file from the internet
xs = np.linspace(0, 30, 31)
ys = [2.3, 3.4, 3.5, 3.5, 3.8, 3.8, 4, 4, 3.9, 3.7, 3.6, 3.5, 3.6, 3.6, 3.5, 3.5, 3.6, 3.5, 2.8, 3, 3.5, 3.8, 4, 3.9, 3.6, 3.5, 3.3, 3.3, 3.2, 3.2, 3.2]

# graph the data
plt.plot(xs, ys, 'b.', markersize = 1)                  # plot the x and y space
plt.fill_between(xs, ys, alpha = 0.2, edgecolor = 'b')  # fill in the space on the graph below the function (integral area)
plt.xlabel("Time (minutes)")                            # label x axis
plt.ylabel("Data Download Speed (Megabits per Second)") # label y axis
plt.title("Download Speed vs Time")                     # graph title
plt.show()                                              # show the graph

for i in range(len(ys)): ys[i] *= 60.0                  # scales the data so its megabits a minute to keep consistent notation
print("\nThe integral of the data download speeds is:\t", simps(ys, xs), "megabits")
