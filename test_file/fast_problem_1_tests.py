import unittest
from assignment1 import fuse
    
class TestProblem1(unittest.TestCase):
    """
    This contains all staff provided testcases and the faster student provided ones.
    """

    # staff provided - guaranteed accurate
    def test_example_1(self):
        got = fuse([[0, 29, 0.9], [0.9, 91, 0.8], [0.8, 48, 0]])
        expected = 126
        self.assertEqual(expected, got, f"expected {expected}, got {got}")

    def test_example_2(self):
        got = fuse([[0, 48, 0.8], [0.8, 91, 0.9], [0.9, 29, 0]])
        expected = 126
        self.assertEqual(expected, got, f"expected {expected}, got {got}")
    
    def test_example_3(self):
        got = fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 50, 0]])
        expected = 24
        self.assertEqual(expected, got, f"expected {expected}, got {got}")

    def test_example_4(self):
        got = fuse([[0, 50, 0.6], [0.6, 50, 0.3], [0.3, 50, 0]])
        expected = 48
        self.assertEqual(expected, got, f"expected {expected}, got {got}")
    
    def test_example_5(self):
        got =  fuse([[0, 50, 0.3], [0.3, 50, 0.3], [0.3, 80, 0]])
        expected = 33
        self.assertEqual(expected, got, f"expected {expected}, got {got}")
    
    def test_example_6(self):
        got =  fuse([[0, 50, 0.6], [0.6, 98, 0.4], [0.4, 54, 0.9], [0.9, 6, 0.3],
                    [0.3, 34, 0.5], [0.5, 66, 0.3], [0.3, 63, 0.2], [0.2, 52, 0.5],
                    [0.5, 39, 0.9], [0.9, 62, 0]] )
        expected = 132
        self.assertEqual(expected, got, f"expected {expected}, got {got}")

    # student provided
    def test_example_7(self): # Tanner Aven
        got = fuse([[0,41,0]])
        expected = 41
        self.assertEqual(expected, got, f"expected {expected}, got {got}")
    


    def test_example_8(self): # Nam Pham
        got = fuse([[0, 63, 0.2], [0.2, 52, 0.5],
                [0.5, 39, 0.9], [0.9, 62, 0.1],
                [0.1, 55, 0.3], [0.3, 60, 0.7],
                [0.7, 50, 0.6], [0.6, 45, 0.4],
                [0.4, 48, 0.8], [0.8, 57, 0]]) 
        expected = 105
        self.assertEqual(expected, got, f"expected {expected}, got {got}")

    def test_example_9(self): # Aditya Patel
        got = fuse([[0, 30, 0.6],
            [0.6, 20, 0.2],
            [0.2, 90, 0.9],
            [0.9, 50, 0]])
        expected = 72
        self.assertEqual(expected, got, f"expected {expected}, got {got}")

    )   
    


if __name__ == '__main__':
    unittest.main()
    
    