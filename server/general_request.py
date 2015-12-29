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

def get_sig_request(request, secretkey, baseurl):
    request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])
    print request_str
    sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k]).replace('+','%20').lower()])for k in sorted(request.iterkeys())])
    print sig_str
    sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
    print sig
    return baseurl+request_str+'&signature='+sig


baseurl = url_config.server_url
apikey = user_config.apikey
secretkey = user_config.secretkey

if apikey:
	request={}
	request['command']='listVirtualMachines'
	request['state']='Running'
	request['response']='xml'
	request['apikey']=apikey
	print "request dictionary = %s \n" % request

	req_url=get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"

