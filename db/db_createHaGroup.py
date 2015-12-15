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
import user_config

def get_sig_request(params, secretkey, baseurl):
    request_str='&'.join(['='.join([k,urllib.quote_plus(params[k])]) for k in params.keys()])
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(params[k].lower().replace('+','%20'))])for k in sorted(params.iterkeys())])
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    return baseurl+request_str+'&signature='+sig


baseurl = url_config.db_url
apikey = user_config.apikey
secretkey = user_config.secretkey


instanceid=''										# existing database instance id
slavecount='1'										# 0~2
hamode='Y'											# Y=auto, N=manual
semisync='N'										# when hamode=N and semisync=N, async mode is enabled
hagroupname='edu_ucloudbiz_XX_hagroup!'				# 12~30 character with !@#%^*, this is key for query.


if apikey != "":
	request={}
	request['command']='createHaGroup'
	request['instanceid']=instanceid
	request['slavecount']=slavecount
	request['hamode']=hamode
	request['semisync']=semisync
	request['hagroupname']=hagroupname
	request['response']='xml'
	request['apikey']=apikey

	req_url=get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print ""

