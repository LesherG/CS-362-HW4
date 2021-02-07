#Gavin Lesher
#2/6/2021
import unittest


#-----to test for error handled code, comment the next line(7) and uncomment the line after that (8)-----
import problem1
#import problem1_errorhandled as problem1



class TestProblem1Methods(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(problem1.volume(2), 8)
        self.assertEqual(problem1.volume(1), 1)
        self.assertEqual(problem1.volume(5), 125)
        self.assertEqual(problem1.volume(.25), 0.015625)
        
    def test_volume_value_error(self):    
        with self.assertRaise(ValueError):
            problem1.volume(0)
            problem1.volume(-5)
            
    def test_volume_type_error(self):
        with self.assertRaise(TypeError):
            problem1.volume('a')
            problem1.volume("Hello");
            
        
            
if __name__ == '__main__':
    unittest.main()
