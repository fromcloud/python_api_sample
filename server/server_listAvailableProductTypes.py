#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
사용가능한 VM 상품의 조합 (serviceoffering=스펙, template=OS, diskoffering=디스크)을 
조회합니다.

* deployVirtualMachine call 을 던지기 전에 사용가능한 상품을 조회합니다.
* listAvailableProductTypes call은 zoneid 가 필수 파라미터가 아니지만 필수파라미터처럼 
  전달하는 것이 효율적입니다.
* listAvailableProductTypes call에서 자신이 만든 custom template 은 조회되지 않지만 
  해당 템플릿이 공개이고 해당 존에 복사되어 있는 경우 deployVirtualMachine call의 파라미터로
  전달이 가능합니다. 
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

# Zone List ( listZones API )
# KOR-Central A     : eceb5d65-6571-4696-875f-5a17949f3317
# KOR-Central B     : 9845bd17-d438-4bde-816d-1b12f37d5080
# KOR-Seoul M       : 95e2f517-d64a-4866-8585-5177c256f7c7
# KOR-HA        : dfd6f03d-dae5-458e-a2ea-cb6a55d0d994
# JPN           : 3e8ce14a-09f1-416c-83b3-df95af9d6308
zoneid=''


if apikey:
	request={}
	request['command']='listAvailableProductTypes'
	request['zoneid']=zoneid
	request['response']='xml'
	request['apikey']=apikey
	
	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(req_url)
	#print res.read()
	#res.close()
else:
	print "apikey none"
