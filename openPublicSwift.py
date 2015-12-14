#!/usr/bin/python


import user_config
import url_config

base_url=url_config.storage_url
accesskey=user_config.accesskey
storagesecret=user_config.storagesecret

from subprocess import call
call(["swift", "-A", base_url, "-U", accesskey, "-K", storagesecret, "stat", "container1"])
print
call(["swift", "-A", base_url, "-U", accesskey, "-K", storagesecret, "post", "container1", "-r", ".r:*"])
print
call(["swift", "-A", base_url, "-U", accesskey, "-K", storagesecret, "stat", "container1"])
