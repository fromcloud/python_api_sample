#!/bin/bash

cat > /etc/init.d/interface_up.sh << EOL
#!/bin/bash

dhclient eth1
EOL

chmod +x /etc/init.d/interface_up.sh
update-rc.d interface_up.sh defaults 100
/etc/init.d/interface_up.sh
