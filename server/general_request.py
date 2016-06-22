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
import urlparse
import linecache
import url_config
import user_config


baseurl = url_config.server_url
apikey = user_config.apikey
secretkey = user_config.secretkey

if apikey:
	request={}
	request['command']='listVirtualMachines'
	request['state']='Running'
	request['response']='xml'
	request['apikey']=apikey
	request['signatureVersion']='3'
	print "request dictionary = %s \n" % request

	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"

