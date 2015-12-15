#!/usr/bin/python

import sys
sys.path.insert(0, "../config/")
import swiftclient
import user_config
import url_config
import pprint

base_url=url_config.storage_url
accesskey=user_config.accesskey
storagesecret=user_config.storagesecret


swift = swiftclient.client.Connection( user=accesskey, key=storagesecret, authurl=base_url)

container_name='container1'
object_name='test.mp4'
swift.get_object(container_name, object_name)

print "stat account info"
pprint.pprint(swift.head_account(), width=1)
