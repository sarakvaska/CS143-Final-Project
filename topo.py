from mininet.topo import Topo

class ourTopo(Topo):
    def __init__(self, **opts):
        #If you pass in dictionary with multiple keys ... kwargs
        ''' Initialize topology and default options '''
        Topo.__init__(self, **opts)

        # add hosts
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")
        host4 = self.addHost("h4")
        host5 = self.addHost("h5")
        host6 = self.addHost("h6")
        host7 = self.addHost("h7")

        # add switches
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")
        switch3 = self.addSwitch("s3")
        switch4 = self.addSwitch("s4")
        switch5 = self.addSwitch("s5")
        switch6 = self.addSwitch("s6")
        switch7 = self.addSwitch("s7")

        # # add links between hosts
        # self.addLink(host1, host2, delay = "0ms")
        # self.addLink(host2, host3, delay = "0ms")

        # add links between host and switch
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(host3, switch3)
        self.addLink(host4, switch4)
        self.addLink(host5, switch5)
        self.addLink(host6, switch6)
        self.addLink(host7, switch7)

        # add links between switches
        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)
        self.addLink(switch2, switch4)
        self.addLink(switch2, switch5)
        self.addLink(switch2, switch6)
        self.addLink(switch2, switch7)

topos = { 'custom': ( lambda: ourTopo() ) }
