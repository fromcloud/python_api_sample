#!/usr/bin/python

'''
비동기 call 을 실행한 경우 반환된 jobid 의 상태값을 조회합니다. 

* 조회된 상태값은 jobid를 반환한 원래 호출 api 에 따라 다릅니다. 
* 
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
import urlparse
import linecache
import url_config
import user_config

baseurl = url_config.server_url
apikey = user_config.apikey
secretkey = user_config.secretkey

jobid=""

if apikey:
	request={}
	request['command']='queryAsyncJobResult'
	request['jobid']=jobid
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"

