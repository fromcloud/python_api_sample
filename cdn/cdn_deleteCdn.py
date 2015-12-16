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

baseurl = url_config.cdn_url
apikey = user_config.apikey
secretkey = user_config.secretkey


# download/streaming
# ip address / storage container name
# direct / storage
# jpn / central

cdnid=''

if apikey != "":
	request={}
	request['command']='deleteCdn'
	request['id']=cdnid
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print "apikey none"

