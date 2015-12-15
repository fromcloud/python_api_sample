#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
import urllib2
import urllib
import hashlib
import hmac
import base64
import urlparse
import linecache
import url_config
import ast

def get_sig_request(params, secretkey, baseurl):
    request_str='&'.join(['='.join([k,urllib.quote_plus(params[k])]) for k in params.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(params[k].lower().replace('+','%20'))])for k in sorted(params.iterkeys())])
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    return baseurl+request_str+'&signature='+sig


fabricurl=url_config.fabric_url

hagroupname='edu_ucloudbiz_XX_hagroup!'
sec='1'										# sec : 1 (public), 0 (private)
mode='3'									# mode : 2 (Read), 3 (Read/Write)

finalurl = fabricurl + hagroupname + "&sec=" + sec + "&mode=" + mode
res=urllib2.urlopen(finalurl)
codes = res.read().replace('\u0000','').replace('null','').replace('(', '').replace(')', '')
result=ast.literal_eval(codes)
lst=result['code'].split(':')
res.close()

import MySQLdb as mdb
import sys

hostip=lst[0]
portno=int(lst[1])
username='root'
password='admin12345'
database='sakila'
sql="select title, release_year from film limit 5"

print
print "Host IP = %s" % hostip
print "Host Port = %s" % portno
print

con = mdb.connect(host=hostip, port=portno, user=username, passwd=password, db=database);
cur = con.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
	print row
con.close()
print
