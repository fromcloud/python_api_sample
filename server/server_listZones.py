#!/usr/bin/python

'''
사용가능한 존들의 리스트를 조회합니다.

* 대부분의 서비스는 존에 의존적입니다. 
* 서비스를 provisioning 할 때 어떤 존을 대상으로 할지를 결정하는 것이 우선적인 결정사항입니다.
'''

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

if apikey:
	request={}
	request['command']='listZones'
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"
