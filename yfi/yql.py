import http.client
import urllib.parse

class Yql:

    def __init__(self):
        self.compiled_str = ""
        self.conn = http.client.HTTPSConnection("query.yahooapis.com")
        self.endpoint = "/v1/public/yql?q="
        self.store = "store://datatables.org/alltableswithkeys"
        self.format = "json"

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

    def exec(self):
        s = urllib.parse.quote(self.compiled_str)
        s = "%s%s&env=%s" % (self.endpoint, s, urllib.parse.quote("store://datatables.org/alltableswithkeys"))
        print(s)
        self.conn.request("GET", s)
        r = self.conn.getresponse()
        print(r.read())

