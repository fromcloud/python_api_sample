#!/bin/bash

yum update -y ca-certificates
yum install -y epel-release
yum install -y salt-minion

fqdn=$(hostname -f)
echo "master: $fqdn" >> /etc/salt/minion
chkconfig salt-minion on
service salt-minion start
