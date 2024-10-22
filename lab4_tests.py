import data
import lab4
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #tests the first element function where input is the list and output would be using the function
    def test_first_element_1(self):
        list1 = [[1,2], [3,4]]
        result = lab4.first_element(list1)
        expected = [1, 3]
        self.assertEqual(result,expected)


    def test_first_element_2(self):
        # write a second test here
        # tests the first element function where input is the list and output would be using the function
        input=[[2,3],[5,8],[]]
        result=lab4.first_element(input)
        expected = [2,5]
        self.assertEqual(result, expected)

    # Part 2
    #tests the x coordinate function where input is the list with point coordinate and output would be using the function to check to see if it is right
    def test_x_coordinates_1(self: list[data.Point]):
       points = [Point(3, 6), Point(70, 14), Point(40, 9)]
       result = lab4.x_coordinates(points)
       expected = [3,70,40]
       self.assertEqual(result,expected)
    def test_x_coordinates_2(self: list[data.Point]):
        points= [Point(5,6), Point(6,4),Point(8,9)]
        result = lab4.x_coordinates(points)
        expected= [5,6,8]
        self.assertEqual(result, expected)


    # Part 3
    # tests the are_in_positive_quadrant function where input is the list with point coordinate and output would be using the function to check to see if it is right
    def test_positive_1(self: list[data.Point]):
        points=[Point(7,8),Point(-5,6)]
        result= lab4.are_in_positive_quadrant(points)
        expected=[7,8,6]
        self.assertEqual(result,expected)
    def test_positive_2(self: list[Point]):
        points=[Point(-8,6),Point(-4,8)]
        result= lab4.are_in_positive_quadrant(points)
        expected=[6,8]
        self.assertEqual(result,expected)

    # Part 4
    # Tests the euclidean distance by using two inputs of coordinates and the output is the distance and check to see whether if it is right or not.
    def test_euclidean(self: Point):
        points1=Point(3,4)
        points2=Point(4,5)
        result=lab4.euclidean(points1,points2)
        expected=2**0.5
        self.assertEqual(result,expected)
    def test_euclidean(self: Point):
        points1=Point(6,7)
        points2=Point(8,9)
        result=lab4.euclidean(points1,points2)
        expected=8**0.5
        self.assertEqual(result,expected)

    # Part 5
    # Tests the manhattan distance by using two inputs of coordinates and the output is the manhattan distance and check to see whether if it is right or not.
    def test_manhattan_distance(self:Point):
        points1=Point(3,6)
        points2=Point(5,10)
        result=lab4.manhattan_distance(points1,points2)
        expected=6
        self.assertEqual(result, expected)

    def test_manhattan_distance(self:Point):
        points1=Point(20,80)
        points2=Point(15,60)
        result=lab4.manhattan_distance(points1,points2)
        expected=25
        self.assertEqual(result, expected)

    # Part 6
    # Tests the distance_ all by using one  inputs of coordinates and the output is the distance and check to see whether if it is right or not.
    def test_distance_all(self:Point):
        points=Point(1,1)
        result=lab4.distance_all(points)
        expected=[(2**0.5)]
        self.assertEqual(result, expected)
    def test_distance_all(self:Point):
        points=Point(3,6)
        result=lab4.distance_all(points)
        expected=[(45**0.5)]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
