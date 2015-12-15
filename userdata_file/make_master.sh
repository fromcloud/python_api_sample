#!/bin/bash

yum update -y ca-certificates
yum install -y epel-release
yum install -y git

git clone https://github.com/fromcloud/userdata.git

file_path=/userdata/master_server/install_elk_server
$file_path/install_elasticsearch.sh
$file_path/install_kibana.sh
$file_path/install_nginx.sh
$file_path/install_logstash.sh
$file_path/install_logstash-forwarder.sh

file_path=/userdata/master_server/install_munin_server
$file_path/install_munin.sh

file_path=/userdata/master_server/install_salt_master
$file_path/install_salt_master.sh

file_path=/userdata/master_server/install_cloudmonkey
$file_path/install_cloudmonkey.sh
