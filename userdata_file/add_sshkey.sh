#!/bin/bash

# creating vm, add ssh key to new vm. so you can login without promot to newly created vm.
echo "ssh-rsa AAAAB3NxaC1yc2EAAAABIwAAAQEA6KvYWy54Fp+WZ34SS/cY5uz/BiSSKKw5oE1lIXthMmih+V5kcPyDJwwVNJPUYtHGJtLDvg53UrMyEEGWag5p+OZqkV6k0KcyVbF1oeSmbNiZJ/Bsv4Ofgj3uW6I5S3EYaJpFgGl7hdrwuFhWI8jew2VZWwCdZcqfKB/1UN7brVf1L10waE6Q7bLSRXTJRbcYXejLZyRYG3fIGV117dcq4zR0lwk5G3UTCgwZrpIa6tEGRjziFffK+/DnVwG1ttF/9Ko6aB13nWxjAzkcxj71ylqzXGLiOkycnqN5nwOipS1Jw1Bttp5P+2zpWuRIo1OKH4NOXOmMksSZ0JLJLi2Tew== root@hsw-linux001" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
/sbin/restorecon ~/.ssh ~/.ssh/authorized_keys
