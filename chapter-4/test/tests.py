import unittest
from rational import Rational as Customfloat

class TestRational(unittest.TestCase):
    def test_reduce(self):
        self.assertEqual(Customfloat(3, 3), Customfloat(1, 1))
        self.assertEqual(Customfloat(1, 3), Customfloat(1, 3))
        self.assertEqual(Customfloat(10, 2), Customfloat(5, 1))
        self.assertEqual(Customfloat(-4, 2), Customfloat(-2, 1))
        self.assertEqual(Customfloat(-1, -1), Customfloat(1, 1))
        self.assertEqual(Customfloat(2, -4), Customfloat(-1, 2))
        self.assertEqual(Customfloat(0, 1), Customfloat(0, 1))
        self.assertEqual(Customfloat(0, 10), Customfloat(0, 1))
           
    def test_nul_denum(self):
        with self.assertRaises(Exception):
            Customfloat(1, 0)
            
    def test_negative_denum(self):
        self.assertEqual(Customfloat(1, -1), Customfloat(-1, 1))
            
    def test_add_rational(self):
        self.assertEqual(Customfloat(1, 3) + Customfloat(1, 3), Customfloat(2, 3))
        self.assertEqual(Customfloat(1, 2) + Customfloat(1, 3), Customfloat(5, 6))
        self.assertEqual(Customfloat(2, 2) + Customfloat(3, 3), Customfloat(2, 1))
        self.assertEqual(Customfloat(3, 2) + Customfloat(1, 2), Customfloat(2, 1))
        self.assertEqual(Customfloat(1, 2) + Customfloat(1, 2), Customfloat(1, 1))
        self.assertEqual(Customfloat(-1, 2) + Customfloat(1, 2), Customfloat(0, 1))
        self.assertEqual(Customfloat(0, 2) + Customfloat(0, 1), Customfloat(0, 10))
        
    def test_sub_rational(self):
        self.assertEqual(Customfloat(1, 3) - Customfloat(1, 3), Customfloat(0, 3))
        self.assertEqual(Customfloat(1, 2) - Customfloat(1, 3), Customfloat(1, 6))
        self.assertEqual(Customfloat(4, 2) - Customfloat(3, 3), Customfloat(1, 1))
        self.assertEqual(Customfloat(3, 2) - Customfloat(1, 2), Customfloat(1, 1))
        self.assertEqual(Customfloat(1, 2) - Customfloat(1, 2), Customfloat(0, 1))
        self.assertEqual(Customfloat(-1, 2) - Customfloat(1, 2), Customfloat(-1, 1))
        self.assertEqual(Customfloat(0, 2) - Customfloat(0, 1), Customfloat(0, 10))
        
    def test_un_sub(self):
        self.assertEqual(-Customfloat(1, 3), Customfloat(-1, 3))
        self.assertEqual(-Customfloat(2, 2), Customfloat(-2, 2))
        self.assertEqual(-Customfloat(3, 2), Customfloat(-3, 2))
        self.assertEqual(-Customfloat(-1, 2), Customfloat(1, 2))
        self.assertEqual(-Customfloat(0, 2), Customfloat(0, 2))
        
    def test_mul_rational(self):
        self.assertEqual(Customfloat(1, 3) * Customfloat(1, 3), Customfloat(1, 9))
        self.assertEqual(Customfloat(1, 2) * Customfloat(2, 3), Customfloat(1, 3))
        self.assertEqual(Customfloat(2, 2) * Customfloat(3, 3), Customfloat(1, 1))
        self.assertEqual(Customfloat(0, 2) * Customfloat(1, 2), Customfloat(0, 1))
        self.assertEqual(Customfloat(0, 2) * Customfloat(0, 1), Customfloat(0, 10))
        self.assertEqual(Customfloat(2, 2) * Customfloat(0, 1), Customfloat(0, 10))
        self.assertEqual(Customfloat(-1, 2) * Customfloat(-1, 1), Customfloat(1, 2))
        self.assertEqual(Customfloat(1, 5) * Customfloat(5, 1), Customfloat(1, 1))

    def test_div_rational(self):
        self.assertEqual(Customfloat(1, 3) / Customfloat(1, 3), Customfloat(1, 1))
        with self.assertRaises(Exception):
            self.assertEqual(Customfloat(5, 2) / Customfloat(0, 2), Customfloat(1, 1))
        
        self.assertEqual(Customfloat(0, 2) / Customfloat(1, 3), Customfloat(0, 1))
        self.assertEqual(Customfloat(10, 2) / Customfloat(1, 2), Customfloat(10, 1))
        self.assertEqual(Customfloat(11, 3) / Customfloat(5, 13), Customfloat(143, 15))
        
    def test_mul_int(self):
        self.assertEqual(Customfloat(1, 3) * 1, Customfloat(1, 3))
        self.assertEqual(Customfloat(1, 2) * 2, Customfloat(1, 1))
        self.assertEqual(Customfloat(2, 2) * 3, Customfloat(3, 1))
        self.assertEqual(Customfloat(0, 2) * 1, Customfloat(0, 2))
        self.assertEqual(Customfloat(0, 2) * 0, Customfloat(0, 2))
        self.assertEqual(Customfloat(2, 2) * 0, Customfloat(0, 2))
        self.assertEqual(Customfloat(-1, 2) * (-1), Customfloat(1, 2))
        self.assertEqual(Customfloat(0, 5) * 5, Customfloat(0, 1))
        
    def test_div_int(self):
        self.assertEqual(Customfloat(1, 3) / 1, Customfloat(1, 3))
        self.assertEqual(Customfloat(3, 2) / 3, Customfloat(1, 2))
        self.assertEqual(Customfloat(0, 2) / 1, Customfloat(0, 2))
        self.assertEqual(Customfloat(-1, 2) / (-1), Customfloat(1, 2))
        self.assertEqual(Customfloat(0, 5) / 5, Customfloat(0, 1))
        self.assertEqual(Customfloat(7, 2) / 2, Customfloat(7, 4))
        
        with self.assertRaises(Exception):
            self.assertEqual(Customfloat(2, 2) / 0, Customfloat(0, 2))
            self.assertEqual(Customfloat(0, 2) / 0, Customfloat(0, 2))
    
    def test_add_int(self):
        self.assertEqual(Customfloat(1, 3) + 1, Customfloat(4, 3))
        self.assertEqual(Customfloat(2, 2) + 3, Customfloat(4, 1))
        self.assertEqual(Customfloat(0, 2) + 1, Customfloat(1, 1))
        self.assertEqual(Customfloat(0, 2) + 0, Customfloat(0, 2))
        self.assertEqual(Customfloat(2, 2) + 0, Customfloat(2, 2))
        self.assertEqual(Customfloat(-1, 2) + 1, Customfloat(1, 2))
        self.assertEqual(Customfloat(-1, 1) + 1, Customfloat(0, 1))
        self.assertEqual(Customfloat(1, 1) + (-1), Customfloat(0, 1))
        self.assertEqual(Customfloat(2, 1) + (-1), Customfloat(1, 1))

    def test_str_(self):
        self.assertEqual(str(Customfloat(1, 2)), '1/2')
        self.assertEqual(str(Customfloat(2, 2)), '1/1')
        self.assertEqual(str(Customfloat(3, 2)), '3/2')
        self.assertEqual(str(Customfloat(-1, 2)), '-1/2')
        self.assertEqual(str(Customfloat(0, 10)), '0/1')
        self.assertEqual(str(Customfloat(-0, 10)), '0/1')
        self.assertEqual(str(Customfloat(-13, 25)), '-13/25')
        self.assertEqual(str(Customfloat(13, -25)), '-13/25')
        
        
if __name__ == '__main__':
    unittest.main()
