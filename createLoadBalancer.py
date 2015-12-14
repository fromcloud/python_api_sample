#!/usr/bin/python

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

def get_sig_request(params, secretkey, baseurl):
    request_str='&'.join(['='.join([k,urllib.quote_plus(params[k])]) for k in params.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(params[k].lower().replace('+','%20'))])for k in sorted(params.iterkeys())])
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    return baseurl+request_str+'&signature='+sig


baseurl = url_config.lb_url
apikey = user_config.apikey
secretkey = user_config.secretkey

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

lbname=id_generator()

# Zone List ( listZones API )
# KOR-Central A     : eceb5d65-6571-4696-875f-5a17949f3317
# KOR-Central B     : 9845bd17-d438-4bde-816d-1b12f37d5080
# KOR-Seoul M       : 95e2f517-d64a-4866-8585-5177c256f7c7
# KOR-HA        : dfd6f03d-dae5-458e-a2ea-cb6a55d0d994
# JPN           : 3e8ce14a-09f1-416c-83b3-df95af9d6308
zoneid='9845bd17-d438-4bde-816d-1b12f37d5080'


if apikey != "":
	request={}
	request['command']='createLoadBalancer'
	request['zoneid']=zoneid
	request['name']=lbname
	request['loadbalanceroption']='roundrobin'
	request['serviceport']='80'
	request['servicetype']='http'
	request['healthchecktype']='tcp'
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print "apikey none"
