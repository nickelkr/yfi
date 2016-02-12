import http.client
import urllib.parse
import json

class Yql:

    def __init__(self):
        self.terms = []
        self.compiled_str = None
        self.conn = http.client.HTTPSConnection("query.yahooapis.com")
        self.endpoint = "/v1/public/yql?q="
        self.store = "store://datatables.org/alltableswithkeys"
        self.format = "json"
        self.table = 'yahoo.finance.quotes'

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def get_endpoint(self):
        return self.endpoint

    def set_table(self, table):
        self.table = table

    def get_table(self):
        return self.table

    def set_store(self, store):
        self.store = "store://%s" % store

    def get_store(self):
        return self.store

    def set_format(self, fmt):
        """This should probably be restricted to xml or json"""
        self.format = fmt

    def get_format(self):
        return self.format

    def parts(self):
        """Return the individual parts of the statement in an array"""
        return self.terms

    def select(self, *itms):
        """Joins the items to be selected and inserts the current table name"""
        if not itms:
            itms = ['*']
        self.terms.append("select %s from %s" % (', '.join(itms), self.table))
        return self

    def where(self, whrs):
        """Build the where clause"""
        self.terms.append("where %s" % whrs)
        return self

    def _in(self, *lst):
        """Build out the in clause. Using _in due to shadowing for in"""
        self.terms.append('in (%s)' % ', '.join(['"%s"' % x for x in lst]))
        return self

    def _and(self):
        self.terms.append('and')
        return self

    def eq(self, i):
        self.terms.append('= %s' % i)

    def compile(self):
        """Take all of the 'parts' components and build the complete query to be passed
           to Yahoo YQL"""
        cs = ""
        for term in self.terms:
            if cs:
                cs += " "
            cs += term
        self.compiled_str = urllib.parse.quote(cs)
        return self

    def symbol(self, *syms):
        """Shortcut for getting everything on 'symbol'. This will use the table that is
           currently set"""
        self.select('*').where('symbol')._in(syms)
        return self

    def compiled(self):
        """Return the compiled str for the user to see. This will already be URL encoded
           though"""
        return self.compiled_str

    def run(self):
        """Execute the query inside of self.compiled_str. This method returns a JSON
           object for easy manipulation unless another format is specified"""
        self.compile()

        s = "%s&format=%s" % (self.compiled_str, self.format)
        s = "%s%s&env=%s" % (self.endpoint, s, urllib.parse.quote(self.store))

        self.conn.request("GET", s)
        r = self.conn.getresponse()
        r = r.read().decode('UTF-8')
        if self.format is "json":
            return json.loads(r)
        else:
            return r


