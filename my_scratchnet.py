#!/usr/bin/python

"""
Build a simple network from scratch, using mininet primitives.
This is more complicated than using the higher-level classes,
but it exposes the configuration details and allows customization.

For most tasks, the higher-level API will be preferable.
"""

from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
from mininet.log import setLogLevel, info
from mininet.util import quietRun

from time import sleep

CTLR_IP = '2017:db8::ffaa'
CTLR_PRT = '6653'

def stop_net(controller, cname, switch):
    info( "*** Stopping network\n" )
    controller.cmd( 'kill %' + cname )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.deleteIntfs()
    info( 'Net was removed\n' )

def scratchNet( cname='controller', cargs='-v ptcp:' ):
    "Create network from scratch using Open vSwitch."

    info( "*** Creating nodes\n" )
    controller = Node( 'c0', inNamespace=False )
    switch = Node( 's0', inNamespace=False )
    h0 = Node( 'h0' )
    h1 = Node( 'h1' )

    info( "*** Creating links\n" )
    Link( h0, switch )
    Link( h1, switch )

    info( "*** Configuring hosts\n" )
    h0.setIP( '192.168.123.1/24' )
    h1.setIP( '192.168.123.2/24' )
    info( str( h0 ) + '\n' )
    info( str( h1 ) + '\n' )

    info( "*** Starting network using Open vSwitch\n" )
    controller.cmd( cname + ' ' + cargs + '&' )
    switch.cmd( 'ovs-vsctl del-br dp0' )
    switch.cmd( 'ovs-vsctl add-br dp0' )
    for intf in switch.intfs.values():
        print switch.cmd( 'ovs-vsctl add-port dp0 %s' % intf )

    # Note: controller and switch are in root namespace, and we
    # can connect via loopback interface
    s_cmd = 'ovs-vsctl set-controller dp0 tcp:[{}]:{}'.format(CTLR_IP, CTLR_PRT)
    print s_cmd
    switch.cmd(s_cmd)

    info( '*** Waiting for switch to connect to controller' )
    try:
        while 'is_connected' not in quietRun( 'ovs-vsctl show' ):
            sleep( 1 )
            info( '.' )

        info( '\n' )

        while True:
            info( "*** Running test\n" )
            h0.cmdPrint( 'ping -c1 ' + h1.IP() )
            info("*** Sleep\n")
            sleep(2)
    except KeyboardInterrupt:
        print "Warning: Caught KeyboardInterrupt, stopping network"
        stop_net(controller,cname,switch)


if __name__ == '__main__':
    setLogLevel( 'info' )
    info( '*** Scratch network demo (kernel datapath)\n' )
    Mininet.init()
    scratchNet()
