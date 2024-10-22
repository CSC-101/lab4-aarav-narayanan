import data
from data import Point


# Write your functions for each part in the space below.

# Part 1
# First it takes all the empty spots on the list to create a new list
# then it takes the first value of the list and creates that list
# input: the list as nest list variable and output is the list titled first
def first_element(nest_list):    #i
    filter_empty_list=[lst for lst in nest_list if len(lst)>0]
    first=[list[0] for n in filter_empty_list]
    return first

# Part 2
#takes the first values of the list and creates a new list from that
#input: point coordinates as a list, output is the x coordinates of those entered
def x_coordinates(points: list[Point]):
    return[point.x for point in points]
# Part 3
#checks to see which numbers are positive and creates a new list giving those numbers that are positive
#input is the points as the list and output is the list with positive numbers
def are_in_positive_quadrant(points: list[Point]):
    return [point for point in points if point.x>0 and point.y>0]

# Part 4
#Takes points and returns the distance using the distance formula
# Input is the x and y coordinates and there two inputs and output is the distance between them
def euclidean(point1:Point, point2:Point)->float:
    x_change = point2.x-point1.x
    x_squared=x_change**2
    y_change=point2.y-point1.y
    y_squared = y_change **2
    add= x_squared+y_squared
    return add**0.5

# Part 5
#Takes points and returns the Manhattan distance using the distance formula
# Input is the x and y coordinates and there two inputs and output is the manhattan distance between them
def manhattan_distance(point1:Point, point2:Point)->float:
    x=point1.x-point2.x
    y=point1.y-point2.y
    if x<0:
        x=-x
    if y<0:
        y=-y
    return x+y

# Part 6
#Same as the euclidean distance one where the distance is found with one point from the origin
#Input is the point coordinate and output the distance from 0,0 to that coordinate as a list
def distance_all(points:list[data.Point]):
    return [euclidean(Point(0,0),point) for point in points]
