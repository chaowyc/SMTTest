from MyCSV import *
import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python main.py input_file_path output_file_path"
    else:
        test = MyCSV(sys.argv[1], sys.argv[2])
        print "all file numbers %(num1)d, case numbers %(num2)d" % {'num1' : test.file_nums, 'num2' : test.file_nums / 4}
        test.OutPutToFile()
