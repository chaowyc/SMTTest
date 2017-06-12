#coding:utf-8
import os
from Stack import *
import Switch
from SMTCase2 import *
from Global import *
from collections import OrderedDict
import csv
import sys
from Attr import Attr
from multiprocessing import Pool, Process

class MyCSV2():

    def __init__(self, input_directory, input_csv_file, output_path, b=None):
        self.input_directory = input_directory
        self.input_csv_file = input_csv_file
        self.output_path = output_path
        self.smt_case_dict = dict()
        self.program_dict = dict()
        self.smt_case_status = {0 : "sat", 1 : "unsat", 2 : "unknown"}
        self.whitelists = b
        self.LoadOld()
        self.OpenDirectory()
        self.program = []
        self.multitodo()


    def __isDirecory(self, path):
        return os.path.isdir(path)

    def __isFile(self, path):
        return os.path.isfile(path)

    def __GetCaseName(self, path):
        return os.path.basename(path)

    def __GetProgramName(self, path):
        return os.path.dirname(path).split('/')[-1]


    def OpenDirectory(self):
        self.file_nums = 0
        files_stack = Stack()
        files_stack.push(self.input_directory)
        while not files_stack.isEmpty():
            tmp_file = files_stack.pop()
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
        tmp_program_name = self.__GetProgramName(tmp_file_path)
        global_dict = Global()
        if self.program_dict.has_key(tmp_program_name):
            global_dict = self.program_dict[tmp_program_name]
        else:
            self.program_dict[tmp_program_name] = global_dict

        smt_case_file_name = tmp_file_name.split('.')[0]

        if global_dict.isExist(smt_case_file_name):
            tmp_smt_case = global_dict.get_value(smt_case_file_name)
            tmp_smt_case.Run(tmp_file_path)
        else:
            tmp_smt_case = SMTCase2()
            tmp_smt_case.Run(tmp_file_path)
            global_dict.insert(smt_case_file_name, tmp_smt_case)

    def LoadOld(self):
        with open(self.input_csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                case_name = row['case name']
                solve_time = row['nopush time']
                self.smt_case_dict[case_name] = solve_time


    def multitodo(self):
        print '\n'
        for k in self.program_dict.keys():
            self.program.append(k)

        #p = Pool(18)
        #p.map(self.single, self.program)
        self.Multi()



    def single(self, program_name):
        field_names = ['case name']
        field_names_ml = []
        for item in Attr:
            field_names.append(item)
            field_names_ml.append(item)
        field_names.append("time")
        field_names_ml.append('time')
        print program_name
        counter = 0
        output_file = self.output_path + '/' + str(program_name) + '.csv'
        with open(output_file, 'w') as single:
            writer = csv.DictWriter(single, fieldnames=field_names)
            writer.writeheader()
            output_dict = dict()
            for case_name, case_attr in self.program_dict[program_name].get_iteritems():
                if case_name in self.smt_case_dict.keys():
                    case_attr.operations.append(self.smt_case_dict[case_name])
                    output_dict['case name'] = case_name
                    for i in range(0, len(Attr)):
                        output_dict[Attr[i]] = case_attr.operations[i]

                    writer.writerow(output_dict)
                    output_dict.clear()
                    counter += 1
                    print '\r %(num)d..' % {'num': counter},
        print "\nwrite %(num1)d row data to %(num2)s " % {'num1': counter, 'num2': program_name}

        output_file = self.output_path + '/' + str(program_name) + '.ml'
        with open(output_file, 'w') as single:
            writer = csv.DictWriter(single, fieldnames=field_names_ml)
            output_dict = dict()
            for case_name, case_attr in self.smt_case_dict[program_name].get_iteritems():
                if case_name in self.smt_case_dict.keys():
                    case_attr.operations.append(self.smt_case_dict[case_name])
                    for i in range(0, len(Attr)):
                        output_dict[Attr[i]] = case_attr.operations[i]

                    writer.writerow(output_dict)
                    output_dict.clear()
        print "write %(num1)d row data to %(num2)s ml" % {'num1': counter, 'num2': program_name}

    def Merge(self):
        print '\n'
        program = []
        field_names = ['case name']
        field_names_ml = []
        for item in Attr:
            field_names.append(item)
            field_names_ml.append(item)
        field_names.append("time")
        field_names_ml.append('time')
        for k, v in self.program_dict.iteritems():
            print k
            program.append(k)
            counter = 0
            output_file = self.output_path + '/' + str(k) + '.csv'
            with open(output_file, 'w') as single:
                writer = csv.DictWriter(single, fieldnames=field_names)
                writer.writeheader()
                output_dict = dict()
                for case_name, case_attr in v.get_iteritems():
                    if case_name in self.smt_case_dict.keys():
                        case_attr.operations.append(self.smt_case_dict[case_name])
                        output_dict['case name'] = case_name
                        for i in range(0, len(Attr)):
                            output_dict[Attr[i]] = case_attr.operations[i]

                        writer.writerow(output_dict)
                        output_dict.clear()
                        counter += 1
                        print '\r %(num)d..' % {'num':counter} ,
            print "\nwrite %(num1)d row data to %(num2)s " %{'num1':counter, 'num2':k}

            output_file = self.output_path + '/' + str(k) + '.ml'
            with open(output_file, 'w') as single:
                writer = csv.DictWriter(single, fieldnames=field_names_ml)
                output_dict = dict()
                for case_name, case_attr in v.get_iteritems():
                    if case_name in self.smt_case_dict.keys():
                        case_attr.operations.append(self.smt_case_dict[case_name])
                        for i in range(0, len(Attr)):
                            output_dict[Attr[i]] = case_attr.operations[i]

                        writer.writerow(output_dict)
                        output_dict.clear()
            print "write %(num1)d row data to %(num2)s ml" % {'num1': counter, 'num2': k}


        for i in range(0, len(program)):
            output_file = self.output_path + '/b_' + str(program[i]) + '.csv'
            counter = 0
            with open(output_file, 'w') as multi:
                writer = csv.DictWriter(multi, fieldnames=field_names)
                writer.writeheader()
                output_dict = dict()
                for j in range(0, len(program)):
                    if i == j:
                        continue
                    else:
                        for case_name, case_attr in self.program_dict[program[j]].get_iteritems():
                            if case_name in self.smt_case_dict.keys():
                                case_attr.operations.append(self.smt_case_dict[case_name])
                                output_dict['case name'] = case_name
                                for i in range(0, len(Attr)):
                                    output_dict[Attr[i]] = case_attr.operations[i]

                                writer.writerow(output_dict)
                                output_dict.clear()
                                counter += 1
                                print '\r %(num)d..' % {'num': counter},
            print "write %(num1)d row data to b_%(num2)s " % {'num1':counter, 'num2':program[i]}

            output_file = self.output_path + '/b_' + str(program[i]) + '.ml'
            with open(output_file, 'w') as multi:
                writer = csv.DictWriter(multi, fieldnames=field_names_ml)
                output_dict = dict()
                for j in range(0, len(program)):
                    if i == j:
                        continue
                    else:
                        for case_name, case_attr in self.program_dict[program[j]].get_iteritems():
                            if case_name in self.smt_case_dict.keys():
                                case_attr.operations.append(self.smt_case_dict[case_name])
                                for i in range(0, len(Attr)):
                                    output_dict[Attr[i]] = case_attr.operations[i]

                                writer.writerow(output_dict)
                                output_dict.clear()
                                counter += 1
            print "write %(num1)d row data to b_%(num2)s ml" % {'num1': counter, 'num2': program[i]}

    def Multi(self):
        print '\n'
        field_names = ['case name']
        field_names_ml = []
        for item in Attr:
            field_names.append(item)
            field_names_ml.append(item)
        field_names.append("time")
        field_names_ml.append('time')
        for i in range(0, len(self.program)):
            output_file = self.output_path + '/b_' + str(self.program[i]) + '.csv'
            counter = 0
            with open(output_file, 'w') as multi:
                writer = csv.DictWriter(multi, fieldnames=field_names)
                writer.writeheader()
                output_dict = dict()
                for j in range(0, len(self.program)):
                    if i == j:
                        print self.program[i]
                        continue
                    else:
                        for case_name, case_attr in self.program_dict[self.program[j]].get_iteritems():
                            if case_name in self.smt_case_dict.keys():
                                case_attr.operations.append(self.smt_case_dict[case_name])
                                output_dict['case name'] = case_name
                                for ii in range(0, len(Attr)):
                                    output_dict[Attr[ii]] = case_attr.operations[ii]

                                writer.writerow(output_dict)
                                output_dict.clear()
                                counter += 1
                                print '\r %(num)d..' % {'num': counter},
            print "write %(num1)d row data to b_%(num2)s " % {'num1':counter, 'num2':self.program[i]}

            output_file = self.output_path + '/b_' + str(self.program[i]) + '.ml'
            with open(output_file, 'w') as multi:
                writer = csv.DictWriter(multi, fieldnames=field_names_ml)
                output_dict = dict()
                for j in range(0, len(self.program)):
                    if i == j:
                        print self.program[i]
                        continue
                    else:
                        for case_name, case_attr in self.program_dict[self.program[j]].get_iteritems():
                            if case_name in self.smt_case_dict.keys():
                                case_attr.operations.append(self.smt_case_dict[case_name])
                                for ii in range(0, len(Attr)):
                                    output_dict[Attr[ii]] = case_attr.operations[ii]

                                writer.writerow(output_dict)
                                output_dict.clear()
                                counter += 1
            print "write %(num1)d row data to b_%(num2)s ml" % {'num1': counter, 'num2': self.program[i]}

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
