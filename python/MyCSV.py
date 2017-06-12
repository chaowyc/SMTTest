#coding:utf-8
import os
from Stack import *
import Switch
from SMTCase import *
from Global import *    
from collections import OrderedDict
import csv
import sys


class MyCSV():

    def __init__(self, input_directory, output_file, b=None):
        self.input_directory = input_directory
        self.output_file = output_file
        self.smt_dict = Global()
        self.smt_case_status = {0 : "sat", 1 : "unsat", 2 : "unknown"}
        self.whitelists = b
        self.OpenDirectory()



    def __isDirecory(self, path):
        return os.path.isdir(path)

    def __isFile(self, path):
        return os.path.isfile(path)

    def __GetCaseName(self, path):
        return path.split('/')[-1]

    def OpenDirectory(self):
        self.file_nums = 0
        files_stack = Stack()
        files_stack.push(self.input_directory)
        while not files_stack.isEmpty():
            tmp_file = files_stack.pop()
            if tmp_file.split('/')[-1] in self.whitelists:
                print "%s is skiped.." % tmp_file
                continue
            else:
                if self.__isDirecory(tmp_file):
                    for item in os.listdir(tmp_file):
                        if item[0] == '.':
                            pass
                        else:
                            files_stack.push(tmp_file + os.sep + item)
                else:
                    self.file_nums += 1
                    print "\r %d .." % self.file_nums ,
                    self.PutTogether(tmp_file)

    def PutTogether(self, tmp_file_path):
        if not tmp_file_path.endswith('.csv'):
            print "%s is not a csv file" % tmp_file_path
            return

        tmp_file_name = self.__GetCaseName(tmp_file_path)
        smt_case_file_name = tmp_file_name.split('.')[0]
        '''
            tmp_file_path = /chaowyc/z3Guide/QF_BV/asp/xxx.smt2.bv.csv
            tmp_file_name = xxx.smt2.bv.csv
            item_split[0] xxx
            item_split[1] "smt2"
            item_split[2] type:
                            bv : bitvector 1
                            oa : operand   2
                            op : operator  3
                            ts : timespan  4
        '''

        if self.smt_dict.isExist(smt_case_file_name):
            tmp_smt_case = self.smt_dict.get_value(smt_case_file_name)
            tmp_smt_case.Run(tmp_file_path)
        else:
            tmp_smt_case = SMTCase()
            tmp_smt_case.Run(tmp_file_path)
            self.smt_dict.insert(smt_case_file_name, tmp_smt_case)

    def OutPutToFile(self):
        all_attr = []

        with open("Attr.txt", 'r') as attr:
            for line in attr:
                line = line.strip()
                all_attr.append(line)

        #sorted_all_attr = OrderedDict(sorted(all_attr.items(), key=lambda x: x[0]))


        print " "
        print "Attrs number %d " % len(all_attr)

        with open(self.output_file, 'w') as csvfile:

            field_names = ['case name']
            file_names_ml = []
            for key in all_attr:
                field_names.append(key)

            field_names.append('nopush status')

            field_names.append('nopush time')

            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            output_dict = dict()

            counter = 0
            for case_name, case_attr in self.smt_dict.get_iteritems():
                counter += 1
                print "\r %(num1)d / %(num2)d case output" % { 'num1' : counter, 'num2' : self.file_nums / 4 },
                sys.stdout.flush()
                output_dict['case name'] = case_name
                for item in all_attr:
                    if item in case_attr.operations.keys():
                        output_dict[item] = case_attr.operations[item]
                    else:
                        output_dict[item] = 0

                output_dict['nopush status'] = case_attr.time_span['nopush_status']
                output_dict['nopush time'] = case_attr.time_span['nopush_time']

                writer.writerow(output_dict)

        with open(self.output_file + "_ml", 'w') as mlfile:
            file_names_ml = []
            for key in all_attr:
                file_names_ml.append(key)

            file_names_ml.append('nopush status')

            file_names_ml.append('nopush time')


            writer = csv.DictWriter(mlfile, fieldnames=file_names_ml)
            output_dict = dict()
            counter = 0
            for case_name, case_attr in self.smt_dict.get_iteritems():
                counter += 1
                print "\r %(num1)d / %(num2)d case output for ml" % { 'num1' : counter, 'num2' : self.file_nums / 4 },
                sys.stdout.flush()
                for item in all_attr:
                    if item in case_attr.operations.keys():
                        output_dict[item] = case_attr.operations[item]
                    else:
                        output_dict[item] = 0

                output_dict['nopush status'] = case_attr.time_span['nopush_status']
                output_dict['nopush time'] = case_attr.time_span['nopush_time']

                writer.writerow(output_dict)
