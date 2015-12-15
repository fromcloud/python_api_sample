#!/bin/bash

dhclient eth1
echo "dhclient eth1" >>/etc/rc.local
