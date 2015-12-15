#!/bin/bash

yum update -y ca-certificates
yum install -y epel-release
yum install -y salt-minion

echo "master: 1.1.1.1" >> /etc/salt/minion
chkconfig salt-minion on
service salt-minion start
