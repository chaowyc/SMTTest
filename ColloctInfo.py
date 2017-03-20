#coding: utf-8

from z3 import *
import csv
import time
from multiprocessing import Pool, Lock
from multiprocessing import Semaphore
from time import sleep

def nopush_solve(case):
    try:
        #set_param(verbose=15)
        s1 = Solver()
        s1.set("timeout", 10000)
        s1.add(case)

        start = time.clock()
        result1 = s1.check()
        elapsed1 = (time.clock() - start)
        return result1, elapsed1
    except:
        return None


def push_solve(case):
    try:
        #set_param(verbose=15)
        s2 = Solver()
        s2.set("timeout", 10000)
        s2.push()
        s2.add(case)
        start = time.clock()
        result2 = s2.check()
        elapsed2 = (time.clock() - start)
        s2.pop()
        return result2, elapsed2
    except:
        return None

def clu_save(fname):
    # TODO: add execption for handling parsing errors
    try:
        case = parse_smt2_file(fname)
        # non-incremental solver
        result1, elapsed1 = nopush_solve(case)
        # incremental solver
        result2, elapsed2 = push_solve(case)
        #string = fname.split('Z3SMT')[1] + " ," + result1 + " ," + elapsed1 + " ," + result2 + " ," + elapsed2

        #semaphore.acquire()
        with lock:
            #print fname.split('Z3SMT')[1], result1, elapsed1, result2, elapsed2
            string = fname.split('Sage2')[1] + ", " + str(result1) + ", " + str(elapsed1) + ", " + str(result2) + ", " + str(elapsed2)
            print string
            sys.stdout.flush()
            output = open('result_sage2.csv', 'a+')
            #print >> output, string
            output.writelines(string)
            output.write("\n")
            output.flush()
            output.close()
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly

def run_smt2(path):
    flist = []  # path to all smtlib2 files
    for root, dirs, files in os.walk(path):
        for fname in files:
            if os.path.splitext(fname)[1] == '.smt2':
                # we can delete unneeded path information later when writing results to report file.
                # e.g. given "/home/jack/test/QF_BV/12434/test.smt2", keep only "QF_BV/12434/test.smt2"
                flist.append(os.path.join(root, fname))
    try:
        pool = Pool(4)
        pool.map_async(clu_save, flist)
    except KeyboardInterrupt:
        pool.close()
        pool.terminate()
        pool.join()
    pool.close()
    pool.join()

if __name__ == "__main__":

    lock = Lock()
    output = open('result.csv', 'a+')
    output.writelines('constraint' + "\t" + 'non-inc result\t' + 'non-inc time\t' + 'inc result\t'+'inc time\n')
    output.flush()
    output.close()
    #run_smt2("/home/chaowyc/z3Guide/QF_BV")
    #run_smt2("/home/chaowyc/PycharmProjects/Z3SMT/smt2")
    run_smt2("/home/chaowyc/z3Guide/Sage2")
