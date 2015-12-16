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


import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

instancename=id_generator()
storagesize='50'				# 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300 (GB)
perfclass='2x2'					# 0.37X0.5, 1X1, 1X2, 2X2, 2X4, 4X4, 4X8, 8X8, 8X16, 8X32, 12X16, 12X32 (vCoreXGB)
maintenanceweekday='sun'		# sunday
parametergroupid='21'			# 21 = mysql5.6.24_default1_small, 22 = mysql5.6.25_default_medium, 23 = mysql5.6.24_default1_large
dbmastername='root'				# mysql admin account
dbmasterpassword='admin12345'	# mysql admin password
dbname='sakila'					# mysql database name
dbengineversion='5.6.24'		# mysql version
usageplantype='hourly'			# billing period = hourly, monthly
zone='kr-2'						# kr-0 (Seoul-M), kr-1 (Central-A), kr-2 (Central-B)


if apikey != "":
	request={}
	request['command']='createInstance'
	request['instancename']=instancename
	request['perfclass']=perfclass
	request['storagesize']=storagesize
	request['maintenanceweekday']=maintenanceweekday
	request['parametergroupid']=parametergroupid
	request['dbmastername']=dbmastername
	request['dbmasterpassword']=dbmasterpassword
	request['dbname']=dbname
	request['dbengineversion']=dbengineversion
	request['usageplantype']=usageplantype
	request['zone']=zone
	request['response']='xml'
	request['apikey']=apikey

	req_url=ucloudbiz.get_sig_request(request, secretkey, baseurl)
	print "Request URL = %s\n" % req_url
	#res=urllib2.urlopen(final_req)
	#print res.read()
	#res.close()
else:
	print ""

