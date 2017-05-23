/etc/init.d/openvswitch-switch restart
IF='eth1'
IP=2017:db8::f101/120
GW=2017:db8::f1ff
IP_CTLR=2017:db8::ffaa

#add bridge
ovs-vsctl add-br br-int
ovs-vsctl add-port br-int $IF
ifconfig $IF 0
#Zero out your eth0 interface and slap it on the bridge interface
#(warning will clip you unless you script it)
#ifconfig br-int 192.168.1.208 netmask 255.255.255.0
ip -6 a a $IP dev br-int
#route add default gw 192.168.1.1 br-int
ip -6 r a default via $GW dev br-int
rip -6 r d default via $GW dev $IF
ovs-vsctl set-controller br-int tcp:$IP_CTLR:6633
# show status
ovs-vsctl show

