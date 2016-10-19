#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
sys.path.insert(0, "../ucloudbiz/")
import ucloudbiz
import urllib2
import urllib
import hashlib
import hmac
import base64
#import os
import urlparse
import linecache
import url_config
import user_config

baseurl = url_config.server_url
apikey = user_config.apikey
secretkey = user_config.secretkey

# Zone List ( listZones API )
# KOR-Central A     : eceb5d65-6571-4696-875f-5a17949f3317
# KOR-Central B     : 9845bd17-d438-4bde-816d-1b12f37d5080
# KOR-Seoul M       : 95e2f517-d64a-4866-8585-5177c256f7c7
# KOR-HA        : dfd6f03d-dae5-458e-a2ea-cb6a55d0d994
# JPN           : 3e8ce14a-09f1-416c-83b3-df95af9d6308
zoneid='9845bd17-d438-4bde-816d-1b12f37d5080'

# Service Offering List ( listServiceOfferings API )
# 1x1 ServiceOffering : c504e367-20d6-47c6-a82c-183b12d357f2
#serviceofferingid='c504e367-20d6-47c6-a82c-183b12d357f2'
serviceofferingid='d00301b7-1965-4ba7-9c18-450b65409163'

# Template List ( listTemplates API )
# CentOS6.5 64bit Template : 42004277-7cf4-4ef1-be28-024a187ea0f8
templateid='42004277-7cf4-4ef1-be28-024a187ea0f8'

name=''
displayname=''

if apikey:
	request={}
	request['command']='deployVirtualMachine'
	request['serviceofferingid']=serviceofferingid
	request['templateid']=templateid
	request['zoneid']=zoneid
	request['name']=name
	request['displayname']=displayname
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"
