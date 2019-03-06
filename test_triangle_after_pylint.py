"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    '''Unit test class'''
    # define multiple sets of tests as functions with names that begin

    def test_right_triangle_a(self):
        '''test 1'''
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        '''test 2'''
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right',
                         '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        '''test 3'''
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def test_tri_a(self):
        '''test 4'''
        self.assertEqual(classifyTriangle(5, 5, 5),
                         'Equilateral', '5,5,5 is equilateral')

    def test_tri_b(self):
        '''test 5'''
        self.assertEqual(classifyTriangle(3, 3, 4), 'Isoceles',
                         '3,3,4, is a Isoceles triangle')

    def test_tri_c(self):
        '''test 6'''
        self.assertEqual(classifyTriangle(5, 6, 7), 'Scalene',
                         '5,6,7 is a scalene triangle')

    def test_tri_d(self):
        '''test 7'''
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right',
                         '5,12,13 is a right triangle')

    def test_tri_e(self):
        '''test 8'''
        self.assertEqual(classifyTriangle(10, 2, 3),
                         'NotATriangle', '10,2,3 is not a triangle')

    def test_tri_f(self):
        '''test 9'''
        self.assertEqual(classifyTriangle(5, 5, 5.5), 'InvalidInput',
                         '5.5, 5.5, 5.5 is invalid as it takes only int and not float')

    def test_tri_g(self):
        '''test 10'''
        self.assertEqual(classifyTriangle(1000, 1000, 1000), 'InvalidInput')

    def test_tri_h(self):
        '''test 11'''
        self.assertEqual(classifyTriangle(1, 1, -1), 'InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
