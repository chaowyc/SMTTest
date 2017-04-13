import sys
import os
from Stack import *
import shutil

def isDirectory(file_dir):
    return os.path.isdir(file_dir)

def OpenDir(file_dir):
    file_nums = 0
    file_list = []
    files_stack = Stack()
    files_stack.push(file_dir)
    while not files_stack.isEmpty():
        tmp_file = files_stack.pop()
        if isDirectory(tmp_file):
            for item in os.listdir(tmp_file):
                if item[0] == '.':
                    pass
                else:
                    files_stack.push(tmp_file + os.sep + item)
        else:
            file_nums += 1
            file_list.append(tmp_file)
    return file_list, file_nums

def ResDir(file_dir):
    tmp = []
    if file_dir[-1] == '/':
        tmp = file_dir[0 : -1]
    else:
        tmp = file_dir
    path, name = os.path.split(tmp)
    return path, name

def Index(num):
    if num < 10:
        return "0"+str(num)
    else:
        return str(num)

def Cut(file_dir, sub_file_nums, all_file_list, all_file_nums):

    sub_file_nums = int(sub_file_nums)

    output_dir, output_name = ResDir(file_dir)
    output_path = output_dir + os.sep + output_name + "_cuted"
    os.mkdir(output_path)

    sub_dir_nums = (all_file_nums / sub_file_nums ) + 1
    counter = 0
    if sub_dir_nums <= 1:
        for items in all_file_lists:
            shutil.copy(items, output_path)
    else:
        index = 1
        tmp = output_path + os.sep + Index(index)
        os.mkdir(tmp)
        for items in all_file_lists:
            counter += 1
            if counter > sub_file_nums:
                counter = 1
                index += 1
                tmp = output_path + os.sep + Index(index)
                os.mkdir(tmp)
            shutil.copy(items, tmp)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Uasge: python CutData.py file_dir"
    else:
        all_file_lists, all_file_nums = OpenDir(sys.argv[1])
        print "%(num)d files" % {'num' : all_file_nums}
        num = raw_input("sub_file_nums ->: ")
        Cut(sys.argv[1], num, all_file_lists, all_file_nums)