from z3 import *

res = open("result.txt", 'w+')
case = parse_smt2_file('/home/chaowyc/z3Guide/QF_BV/asp/15Puzzle/2016479/15-puzzle.init6.smt2')

print case