'''
    class of smtcase

'''
class SMTCase2():
    def __init__(self):
        self.operations = []
        self.file_counter = 0

    def Run(self, file_path):
        self.file_path = file_path
        self.OpFile()

    def OpFile(self):
        op_file = open(self.file_path)
        for line in op_file.readlines():
            lines = line.strip()
            self.operations.append(lines)
        op_file.close()
