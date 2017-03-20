from z3 import *
from sys import argv

# read smt2 expression from file
script, filename = argv
smtbst = parse_smt2_file(filename).children()
#print smtbst
# extract features
dic = dict()
for item in smtbst:
    tmp = item.decl()
    print item.decl(), item.decl().kind()
    if tmp in dic.keys():
        dic[tmp] += 1
    else:
        dic[tmp] = 1

print "========"
for key, val in dic.items():
    print key, ":", val

