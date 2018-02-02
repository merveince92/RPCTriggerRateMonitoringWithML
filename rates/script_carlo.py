#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import sys
import time
import re

import cx_Oracle
import string


connstr='cms_dt_elec_conf/cmsonr2008@cms_omds_lb'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=100

if len(sys.argv)==1 :
   query="select * from tm_rates order by datetime desc"

elif len(sys.argv)==4 and sys.argv[1]=="-a" :
   query="INSERT INTO tm_rates VALUES(NULL,'"+sys.argv[2]+"','"+sys.argv[3]+"',CURRENT_TIMESTAMP) "

else :
   print "Usage:",sys.argv[0],"[-a Sector Rate]"
   exit(0)


print query

curs.execute(query)
debug=1
if len(sys.argv)==1 :
    print "Sector   ","Rate   ","Timestamp"
    for rows in curs:
        type=rows[1]
        rel=rows[2]
        arch=rows[3]
        print type,rel,arch
else :
  conn.commit()
