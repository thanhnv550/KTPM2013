import input
import itertools
import unittest
input_file="input.py"
'''
Lay danh sach khoang
input : s='[1;3][...][....]'
output: b= [[1,3],[4,5],.....]
'''
def list_khoang(s):
    s=s.replace('][',',')    #"[1;3,4;5,...]"
    s=s.replace('[','')      #"1;3,4;5,....]"
    s=s.replace(']','')      #"1;3,4;5,..."
    a=s.split(',')           #a=['1;3','4;5','....']
    b=list()
    e=list()
    for i in a:
        e1=list()
        c=i.split(";")       #c=['1','3']
        e1.append(int(c[0]))
        e1.append(int(c[1])) #e1=[1,3]
        b.append(e1)          #b=[[1,3],[4,5],.....]
    b.sort()

    hople=True
    for i in range(0,b.__len__()-1,1):
       if(b[i][1]>=b[i+1][0]):
           hople=False
    if(hople==False):
        return hople
    bnew=list()
    for i in b:
        bnew.append(i[0])
    return bnew

'''
-Chuan hoa input ve dang list:
-Voi truong hop 2 bien:
[[[0, 10], [11, 20], [21, 25], [26, 30]], [[0, 10], [11, 23], [21, 30]]]
'''
def getInputContent():
    f = open(input_file, 'r')
    content=f.read()
    len= str.__len__(content)
    s=list()
    st1= content.find("'''",0,len)+3
    st2= content.find("'''",st1,len)
    contentInput=content[st1:st2]
    contentInput=contentInput.replace(' ','')
    contentInput=contentInput.splitlines()
    for i in contentInput:
        if(i!=''):
            thamso=i.split(':')
            khoangnghiem=list_khoang(thamso[1])
            s.append(khoangnghiem)
    return s

''' My unittest class:
'''
class TestSequense(unittest.TestCase):
    pass

def test_generator(a,b):
    def test(self):
        self.assertEqual(a,b)
    return test

'''Main function:'''
if __name__ == "__main__":

    input_data= getInputContent()

    try:
        a=list(itertools.product(*input_data))
        i=0
        for t in a:
            i=i+1
            test_name = 'test_%s'% i
            test = test_generator(input.main(*t),input.main(*t))
            setattr(TestSequense, test_name, test)

        unittest.main()
    except Exception:
        raise Exception("wrong input")
