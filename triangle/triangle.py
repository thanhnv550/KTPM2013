# return -2: ngoai mien xac dinh.
# return -1: input sai dinh dang.
# return 1: tam giac deu.
# return 2: tam giac vuong can.
# return 3: tam giac can.
# return 4: tam giac vuong.
# return 5: tam giac thuong.
# return 0: khong la tam giac.
import math
import decimal
e=2**-32
maximum=2**31-1
# check_vuong function.
def check_binhphuong(a,b,c):
        c12=decimal.Decimal(math.pow(a,2));
	c22=decimal.Decimal(math.pow(b,2));
	c32=decimal.Decimal(math.pow(c,2));

        if (math.fabs(c12+c22-c32)<=e) or (math.fabs(c22+c32-c12)<=e) or (math.fabs(c32+c12-c22)<=e):
                return True
        else:
                return False

#check_tamgiac function. 
def check_tamgiac(a,b,c):
        if decimal.Decimal(a)+decimal.Decimal(b)>decimal.Decimal(c) and decimal.Decimal(a)+decimal.Decimal(c)>decimal.Decimal(b)and decimal.Decimal(b)+decimal.Decimal(c)>decimal.Decimal(a)and a>0 and b>0 and c>0:
                return True
        else: return False
        
#phan_loai_tamgiac function.        
def detect_triangle(a,b,c):
        try:
                c1=float(a)
                c2=float(b)
                c3=float(c)
        except ValueError:
                return -1
        if(decimal.Decimal(c1)<0 or decimal.Decimal(c2)<0 or decimal.Decimal(c3)<0 or c1>maximum or c2>maximum or c3>maximum):
                return -2
        if check_tamgiac(c1,c2,c3)==True:
                if (c1==c2 or c2==c3 or c3==c1) and check_binhphuong(c1,c2,c3):
                        #print "Tam giac vuong can."
                        return 2 
                elif c1==c2 and c2==c3 and c3==c1:
                        #print "Tam giac deu."
                        return 1
	
                elif c1==c2 or c1==c3 or c2==c3:
                        #print "Tam giac can"
                        return 3
                elif check_binhphuong(c1,c2,c3):
                        #print "Tam giac vuong"
                        return 4
                else:
                        #print "Tam giac thuong"
                        return 5
        else:
                #print "Khong la tam giac"
                return 0
        





        
		
