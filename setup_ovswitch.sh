/etc/init.d/openvswitch-switch restart
#IF='eth1'
IF='enp0s8'
IP=2017:db8::f101/120
GW=2017:db8::f1ff
IP_CTLR=2017:db8::ffaa
OF_PORT=6653

#add bridge
echo "ovs-vsctl add-br br-int"
ovs-vsctl add-br br-int
echo "ovs-vsctl add-port br-int $IF"
ovs-vsctl add-port br-int $IF
echo "ifconfig $IF 0"
ifconfig $IF 0
#Zero out your eth0 interface and slap it on the bridge interface
#(warning will clip you unless you script it)
#ifconfig br-int 192.168.1.208 netmask 255.255.255.0
echo "ip -6 a a $IP dev br-int"
ip -6 a a $IP dev br-int

#route add default gw 192.168.1.1 br-int
echo "ip -6 r a default via $GW dev br-int"
ip -6 r a default via $GW dev br-int

echo "ip -6 r d default via $GW dev $IF"
ip -6 r d default via $GW dev $IF
#set bridge
echo "sudo ovs-vsctl set bridge br-int protocols=OpenFlow13"
sudo ovs-vsctl set bridge br-int protocols=OpenFlow13

echo "ovs-vsctl set-controller br-int tcp:[$IP_CTLR]:"$OF_PORT
ovs-vsctl set-controller br-int tcp:[$IP_CTLR]:$OF_PORT
# show status
echo "ovs-vsctl show"
ovs-vsctl show
echo "ip l s br-int up"
ip l s br-int up
