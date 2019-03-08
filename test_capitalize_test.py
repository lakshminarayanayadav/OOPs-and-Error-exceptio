
import unittest
import capitalize_test

class TestCap(unittest.TestCase):
    
    def test_one_word(self)
        text = 'python'
        result = capitalize_test.capiralize.t(text)
        self.assertEqual(result,'Python')
        
    def test_multipkle_word(self):
        text = "my python"
        result = capitalize_test.capiralize.t(text)
        self.assertEqual(result,'My python')
        
if __name__=='__main__':
    unittest.main()
