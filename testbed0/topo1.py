#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
import netconstants as netconst
from mininet.cli import CLI

def ofp_version(switch, protocols):
    protocols_str = ','.join(protocols)
    command = 'ovs-vsctl set Bridge %s protocols=%s' % (switch, protocols_str)
    switch.cmd(command.split(' '))

if '__main__' == __name__:
    net = Mininet(switch=OVSSwitch)
    c_any = RemoteController('c_any', netconst.CTLR_AC_IP, netconst.PORT_CTLR)
    #c_any = RemoteController('c_any', netconst.CTLR_AC_IP, netconst.PORT_CTLR)
    net.addController(c_any)
    # add switches
    s1 = net.addSwitch('s1')
    # add host
    h1 = net.addHost('h1')
    net.addLink(s1, h1)

    # build net
    net.build()
    net.start()
    # start: Overridden to do nothing.
    c_any.start()
    ofp_version(s1, ['OpenFlow13'])
    # add command line interface
    CLI(net)
