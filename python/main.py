from MyCSV import *
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', nargs=1)
    parser.add_argument('output_path', nargs=1)
    parser.add_argument('-b', nargs=argparse.REMAINDER, default=[])

    arge = parser.parse_args()
    print arge.b
    test = MyCSV(arge.input_path[0], arge.output_path[0], b=arge.b)
    print "all file numbers %(num1)d, case numbers %(num2)d" % {'num1' : test.file_nums, 'num2' : test.file_nums / 4}
    test.OutPutToFile()
