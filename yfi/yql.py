import http.client
import urllib.parse

class Yql:

    def __init__(self):
        self.terms = []
        self.compiled_str = None
        self.conn = http.client.HTTPSConnection("query.yahooapis.com")
        self.endpoint = "/v1/public/yql?q="
        self.store = "store://datatables.org/alltableswithkeys"
        self.format = "json"

    def set_endpoint(self, new):
        self.endpoint = new

    def get_endpoint(self):
        return self.endpoint

    def set_store(self, new):
        self.store = "store://%s" % new

    def get_store(self):
        return self.store

    def set_format(self, fmt):
        self.format = fmt

    def get_format(self):
        return self.format

    def parts(self):
        return self.terms

    def select(self, *itms):
        if not itms:
            itms = ['*']
        self.terms.append("select %s from yahoo.finance.quotes" % ', '.join(itms))
        return self

    def where(self, whrs):
        self.terms.append("where %s" % whrs)
        return self

    def _in(self, *lst):
        self.terms.append('in (%s)' % ', '.join(['"%s"' % x for x in lst]))
        return self

    def _and(self):
        self.terms.append('and')
        return self

    def eq(self, i):
        self.terms.append('= %s' % i)

    def compile(self):
        cs = ""
        for term in self.terms:
            if cs:
                cs += " "
            cs += term
        self.compiled_str = urllib.parse.quote(cs)
        return self

    def symbol(self, *syms):
        self.select('*').where('symbol')._in(syms)
        return self

    def compiled(self):
        return self.compiled_str

    def exec(self):
        if self.compiled_str is None:
            self.compile()

        s = "%s&format=%s" % (self.compiled_str, self.format)
        s = "%s%s&env=%s" % (self.endpoint, s, urllib.parse.quote("store://datatables.org/alltableswithkeys"))

        self.conn.request("GET", s)
        r = self.conn.getresponse()
        print(r.read())

