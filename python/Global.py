class Global():
    def __init__(self):
        self.all_smt_case = dict()

    def insert(self, key, value):
        self.all_smt_case[key] = value

    def isExist(self, key):
        return self.all_smt_case.has_key(key)

    def size(self):
        return len(self.all_smt_case)

    def get_value(self, key):
        if self.isExist(key):
            return self.all_smt_case[key]
        else:
            None

    def get_iteritems(self):
        return self.all_smt_case.iteritems()

    def get_items(self):
        return self.all_smt_case.items()

