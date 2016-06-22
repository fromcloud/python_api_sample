#!/bin/bash

# creating vm, add ssh key to new vm. so you can login without promot to newly created vm.
echo "ssh-rsa 3NxaC1yc2EAAAABIwAAAQEA65nwOipS1Jw1Bttp5P+2zpWuRIo1OKH4NOXOmMksSZ0JLJLi2Tew== root@hsw-linux001" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
/sbin/restorecon ~/.ssh ~/.ssh/authorized_keys
