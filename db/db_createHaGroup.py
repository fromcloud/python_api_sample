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

	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print ""

