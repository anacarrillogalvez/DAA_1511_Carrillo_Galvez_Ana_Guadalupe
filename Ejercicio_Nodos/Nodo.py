
from multiprocessing import Value
from optparse import Values
from turtle import left, right
from typing import ValuesView

class NodoTernario:

    def __init__(self , Values , left= None, center= None, right= None, data = None):
        self.data = Values
        self.left = left
        self.center = center
        self.rigth = right

