#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
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


baseurl = url_config.cdn_url
apikey = user_config.apikey
secretkey = user_config.secretkey


# download/streaming
# ip address / storage container name
# direct / storage
# jpn / central

name='mystreaming'
servicetype='streaming'
addr='container1'
origintype='storage'
zonenm='central'

if apikey != "":
	request={}
	request['command']='createCdn'
	request['name']=name
	request['servicetype']=servicetype
	request['addr']=addr
	request['type']=origintype
	request['zonenm']=zonenm
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print "apikey none"

