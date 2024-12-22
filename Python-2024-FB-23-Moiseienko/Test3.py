#!/usr/bin/python3
import cProfile
from random import getrandbits
from Mathe.gf import *

fld = GF()
BITS = fld.m
A,B,C = getrandbits(BITS),getrandbits(BITS),getrandbits(BITS)
a,b,c = fld(A),fld(B),fld(C)
def add():
    r = a + b
def mul():
    r = a * b 
def pow():
    r = a**b 
def inv():
    r = a.inv()
def trace():    
    r = a.trace()

def main() -> None:
    cProfile.run('add()')
    cProfile.run('mul()')
    cProfile.run('pow()')
    cProfile.run('inv()')
    cProfile.run('trace()')

if __name__ == "__main__":
    main()
