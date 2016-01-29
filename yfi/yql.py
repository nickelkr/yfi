class Yql:

    def __init__(self):
        self.compiled_str = ""

    def select(self, *itms):
        self.compile("select %s from yahoo.finance.quotes" % itms)
        return self

    def where(self, *whrs):
        self.compile("where %s" % whrs)
        return self

    def _in(self, *lst):
        self.compile('in ("%s")' % lst)
        return self

    def compile(self, part):
        if self.compiled_str:
            part = " " + part
        self.compiled_str += part

    def compiled(self):
        return self.compiled_str
