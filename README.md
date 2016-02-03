# YFi
Yahoo! YQL library with tools focusing on the finance portion (eventually).

**Description**

YFi allows you to create and run queries against Yahoo's YQL datatables using a 
object oriented methodology.

It is currently in the beginning stages and supports the following YQL statments:
  - select
  - where
  - in (_in)
  - and (_and)
  - equal (eq)

You can also set YQL variables, the following of which are supported:
  - store
  - table
  - endpoint
  - format

The plan is to also provide tools to use specifically with the finance tables.

**Usage**

The following is a example that returns all the data from the yahoo.finance.quotes table for the symbols 'TSLA' and 'GOOG'
```python
from yfi.yql import Yql
# create a Yql object
y = Yql()
# this object supports chaining so we can build our query in one line. select() defaults to '*'
y.select().where('symbol')._in('TSLA', 'GOOG')
# the exec() method returns a json object unless format has been changed otherwise
j = y.exec()
```
The following is a shortcut for the above. It will select('*') from whatever table is set (default: yahoo.finance.quotes)
for the given symbol(s)
```python
from yfi.yql import Yql
y = Yql()
y.symbol('TSLA', 'GOOG')
j = y.exec()
```
**Upcoming Features**

  - Better error handling
  - Processing of the JSON response into a class that provides facilities for applying analytics easily

**Running Tests**

To run all tests:
python -m unittest discover

To run just Yql:
python -m unittest test.TestYql
