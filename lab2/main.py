from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
from art import *

def main():
    rec = Rectangle('синего', 14, 14)
    cir = Circle('зеленого', 14)
    sq = Square('красного', 14)
    
    print(rec)
    print(cir)
    print(sq)
    
    tprint("PACKAGE", font='isometric1') 

if __name__ == '__main__':
    main()
