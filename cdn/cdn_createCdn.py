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


# ip address / storage container name
# direct / storage

name='mystreaming'
servicetype='streaming'			# download/streaming
origintype='storage'			# direct / storage
addr='container1'				# ip address / storage container name, storage cantainer must be opened to public
zonenm='central'				# jpn / central

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
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print "apikey none"

