'''
    class of smtcase

'''
import csv

class SMTCase():
    def __init__(self):
        self.attributes = dict()
        self.operations = dict()
        self.time_span = dict()
        self.csv_file_status = {"bv" : False, "oa" : False, "op" : False, "ts" : False}
        self.csv_file_type = {"bv": 1, "oa": 2, "op": 3, "ts": 4}
        self.file_counter = 0

    def __FileType(self):
        self.file_name = self.file_path.split('/')[-1]
        items = self.file_name.split('.')
        self.case_name = items[0]
        self.file_type = items[2]

    def __GetCsvFileType(self, type):
        return self.csv_file_type[type]

    def Run(self, file_path):
        self.file_path = file_path
        self.__FileType()

        if self.__GetCsvFileType(self.file_type) == 1:
            self.file_counter += 1
            self.BvFile()
        elif self.__GetCsvFileType(self.file_type) == 2:
            self.file_counter += 1
            self.OaFile()
        elif self.__GetCsvFileType(self.file_type) == 3:
            self.file_counter += 1
            self.OpFile()
        elif self.__GetCsvFileType(self.file_type) == 4:
            self.file_counter += 1
            self.TsFile()

    def CaseStatus(self):
        if self.file_counter == 4 and self.csv_file_status['bv'] and self.csv_file_status['oa'] and self.csv_file_status['op'] and self.csv_file_status['ts']:
            return True
        return False

    def BvFile(self):
        return

    def OaFile(self):
        return

    def OpFile(self):
        if self.csv_file_status['op']:
            return
        else:
            self.csv_file_type['op'] = True
            op_file = open(self.file_path)
            for line in op_file.readlines():
                if line.strip() == "summary:" or line.startswith('numbers'):
                    continue
                lines = line.strip().split(':')
                op = lines[0]
                num = lines[1]
                self.operations[op] = num
            op_file.close()


    def TsFile(self):
        if self.csv_file_status['ts']:
            return
        else:
            self.csv_file_type['ts'] = True
            with open(self.file_path) as tsfile:
                for row in tsfile.readlines():
                    if row.startswith('push'):
                        continue
                    items = row.strip().split('\t')
                    self.time_span['nopush_status'] = items[0]
                    self.time_span['nopush_time'] = items[1]
