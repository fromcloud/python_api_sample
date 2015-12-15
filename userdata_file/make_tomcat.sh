#!/bin/bash

yum update -y ca-certificates
yum install -y epel-release
yum install -y salt-minion

domain=$(hostname -f | awk -F'.' '{print $2"."$3}')
echo "master: master.$domain" >> /etc/salt/minion
chkconfig salt-minion on
service salt-minion start
