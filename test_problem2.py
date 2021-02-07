#Gavin Lesher
#2/6/2021
import unittest

import problem2



class TestProblem2Methods(unittest.TestCase):
    def test_average(self):
        self.assertEqual(problem2.average([0,1,2]), 1)
        self.assertEqual(problem2.average([2,-4]), -1)
        self.assertEqual(problem2.average([134]), 134)
        self.assertEqual(problem2.average([0,1,2,3,4,5,6,7,8,9]), 4.5)
        self.assertEqual(problem2.average({1,3}), 2)
        
    def test_average_list_errors(self):
        with self.assertRaises(ZeroDivisionError):
            problem2.average([])
            
    def test_average_type_errors(self):
        with self.assertRaises(TypeError):
            problem2.average('a')
            problem2.average(["test", "test2"])
        
            
if __name__ == '__main__':
    unittest.main()
