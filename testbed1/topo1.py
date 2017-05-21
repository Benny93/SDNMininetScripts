#!/usr/bin/python

import readline
from mininet.topo import Topo

class MyTopo( Topo ):
    def __init__(self):
        #init topo  
        Topo.__init__( self)
        #Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost('h2')
        s1 = self.addSwitch( 's3' )
        s2 = self.addSwitch('s4')
        

        #links
        self.addLink( h1 , s1)
        self.addLink(h2,s2)
        self.addLink(s1,s2)

topos={'mytopo' : ( lambda: MyTopo())}
