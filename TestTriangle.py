# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: srikanth
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testTriA(self):
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is equilateral')

    def testTriB(self):
        self.assertEqual(classifyTriangle(3,3,4),'Isoceles','3,3,4, is a Isoceles triangle')
    
    def testTriC(self):
        self.assertEqual(classifyTriangle(5,6,7),'Scalene', '5,6,7 is a scalene triangle')
    
    def testTriD(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a right triangle')
    
    def testTriE(self):
        self.assertEqual(classifyTriangle(10,2,3),'NotATriangle','10,2,3 is not a triangle')
    
    def testTriF(self):
        self.assertEqual(classifyTriangle(5,5,5.5),'InvalidInput','5.5, 5.5, 5.5 is invalid as it takes only int and not float')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
    
    
