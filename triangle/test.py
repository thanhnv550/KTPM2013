import unittest
import math
maximum=2**31-1
from triangle import detect_triangle
class Test(unittest.TestCase):
        def setUp(self):
            pass
 
        def test_saikieu_input1(self):
            self.assertEqual(detect_triangle('abc',7.5,8.6), -1)
            
        def test_saikieu_input2(self):
            self.assertEqual(detect_triangle(7.1,'abc',8.3), -1)
            
        def test_saikieu_input3(self):
            self.assertEqual(detect_triangle(7.3,8.2,'abc'), -1)
        
        def test_saikieu_input4(self):    
            self.assertEqual(detect_triangle('abc',9,-7), -1)
            
        def test_saikieu_input5(self):    
            self.assertEqual(detect_triangle('abc',maximum+1,9), -1)
            
        
        def test_gioihan_input1(self):    
            self.assertEqual(detect_triangle(-1,7,8), -2)
        def test_gioihan_input1_1(self): 
            self.assertEqual(detect_triangle('-1',7,8), -2)
            
        def test_gioihan_input2(self):
            self.assertEqual(detect_triangle(7,-7,8), -2)
        def test_gioihan_input2_2(self):
            self.assertEqual(detect_triangle(7,'-7',8), -2)
        def test_gioihan_input3(self):
            self.assertEqual(detect_triangle(7,9,-7), -2)
        def test_gioihan_input3_3(self):
            self.assertEqual(detect_triangle(7,9,'-7'), -2)
            
        
        def test_gioihan_input4(self):    
            self.assertEqual(detect_triangle(maximum+1,7,9), -2)
        def test_gioihan_input5(self):    
            self.assertEqual(detect_triangle(7,maximum+1,9), -2)
        def test_gioihan_input6(self):    
            self.assertEqual(detect_triangle(7,9,maximum+1), -2)
        def test_gioihan_input7(self):    
            self.assertEqual(detect_triangle(-math.pow(2,-31),9,maximum), -2)
        def test_gioihan_input8(self):    
            self.assertEqual(detect_triangle(9,-math.pow(2,-31),maximum), -2)
        def test_gioihan_input9(self):    
            self.assertEqual(detect_triangle(9,maximum,-math.pow(2,-31)), -2)
            
        def test_tamgiacdeu1(self):
            self.assertEqual(detect_triangle(1,1,1), 1)
            self.assertEqual(detect_triangle(math.sqrt(6),math.sqrt(6),math.sqrt(6)), 1)
            self.assertEqual(detect_triangle(maximum,maximum,maximum), 1)
            self.assertEqual(detect_triangle(math.pow(2,-10),math.pow(2,-10),math.pow(2,-10)), 1)
        def test_tamgiacdeu2(self):    
            self.assertEqual(detect_triangle('4','4','4'), 1)
        def test_tamgiacdeu3(self):    
            self.assertEqual(detect_triangle('4.5',4.5,4.5), 1)
        def test_tamgiacdeu4(self):                     
            self.assertEqual(detect_triangle(4.5,'4.5',4.5), 1)
        def test_tamgiacdeu5(self):                     
            self.assertEqual(detect_triangle(4.5,4.5,'4.5'), 1)
        
            
        def test_tamgiacvuong1(self):
            self.assertEqual(detect_triangle(3,5,4), 4)
        def test_tamgiacvuong1_1(self):
            self.assertAlmostEqual(detect_triangle(math.sqrt(89),5,8), 4)
        def test_tamgiacvuong2(self):
            self.assertEqual(detect_triangle(4,3,5), 4)
        def test_tamgiacvuong3(self):
            self.assertEqual(detect_triangle(5,4,3), 4)
        def test_tamgiacvuong4(self):
            self.assertEqual(detect_triangle('5','3','4'), 4)
            
            
        def test_tamgiaccan1(self):
            self.assertEqual(detect_triangle(5.6,5.6,3), 3)
        def test_tamgiaccan1_2(self):
            self.assertEqual(detect_triangle(maximum,2, maximum) , 3)
        def test_tamgiaccan1_1(self):
            self.assertEqual(detect_triangle(2**26,2**-10, 2**26) , 3)
        def test_tamgiaccan2(self):
            self.assertEqual(detect_triangle(5.6,3,5.6), 3)
        def test_tamgiaccan3(self):
            self.assertEqual(detect_triangle(3,5.6,5.6), 3)            
        def test_tamgiaccan4(self):
            self.assertEqual(detect_triangle('5','5','3'), 3)
                             
        def test_tamgiacvuongcan1(self):
            self.assertEqual(detect_triangle(math.sqrt(2),1,1), 2)
        def test_tamgiacvuongcan2(self):
            self.assertEqual(detect_triangle(1,math.sqrt(2),1), 2)
        def test_tamgiacvuongcan3(self):
            self.assertEqual(detect_triangle(1,1,math.sqrt(2)), 2)
            
        def test_khonglatamgiac1(self):
            self.assertEqual(detect_triangle(2,1,1), 0)
            self.assertEqual(detect_triangle('2','1','1'), 0)
        def test_khonglatamgiac2(self):
            self.assertEqual(detect_triangle(0,1,1), 0)
            self.assertEqual(detect_triangle('0','1','1'), 0)
        def test_khonglatamgiac3(self):
            self.assertEqual(detect_triangle(1,0,1), 0)
            self.assertEqual(detect_triangle('1','0','1'), 0)
        def test_khonglatamgiac4(self):
            self.assertEqual(detect_triangle(1,1,0), 0)
        def test_khonglatamgiac5(self):
            self.assertEqual(detect_triangle('1','1','0'), 0)
            
        def test_tamgiacthuong1(self):
            self.assertEqual(detect_triangle(3,4,6), 5)
        def test_tamgiacthuong2(self):
            self.assertEqual(detect_triangle(6*math.pow(2,-15), 4*math.pow(2,-15), 7*math.pow(2,-15)), 5)
        def test_tamgiacthuong3(self):
            self.assertEqual(detect_triangle(maximum,maximum-1,maximum-2), 5)
        def test_tamgiacthuong4(self):
            self.assertEqual(detect_triangle('6','7','8'), 5)
        
            
             
            
                    
if __name__ == '__main__':
    unittest.main()
