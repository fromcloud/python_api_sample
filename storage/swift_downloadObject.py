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
# get object

print "start download object"
container_name='container1'
object_name='test.mp4'
obj_tuple=swift.get_object(container_name, object_name)
with open(object_name, 'w') as my_obj:
        my_obj.write(obj_tuple[1])

print "end download object"

print "list containers"
pprint.pprint(swift.head_account(), width=1)

print

print "list object in ther container"
pprint.pprint(swift.head_container(container_name), width=1)
