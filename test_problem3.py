#Gavin Lesher
#2/6/2021
import unittest


#-----to test for error handled code, comment the next line(7) and uncomment the line after that (8)-----
#import problem3
import problem3_errorhandled as problem3


class TestProblem3Methods(unittest.TestCase):
    def test_first_and_last(self):
        self.assertEqual(problem3.first_and_last("Mike", "Meyers"), "Mike Meyers")

    def test_first_and_last_type_error(self):
        with self.assertRaises(TypeError):
            problem3.first_and_last("Test", 87)
            
    def test_first_and_last_empty_string(self):
        with self.assertRaises(ValueError):
            problem3.first_and_last("", "lastname")
            problem3.first_and_last("firstname", "")
            
if __name__ == '__main__':
    unittest.main()