class Yql:

    def __init__(self):
        self.statment = {'select': [],
                         'where': [],
                         'in': []}

    def select(self, *itms):
        self.statment['select'].append(itms)
        return self

    def selects(self):
        return self.statment['select']

    def where(self, *whrs):
        self.statment['where'].append(whrs)
        return self

    def wheres(self):
        return self.statment['where']

    def _in(self, *lst):
        self.statment['in'].append(lst)
        return self

    def _ins(self):
        return self.statment['in']