from mininet.topo import Topo

class ourTopo(Topo):
    def __init__(self, **opts):
        #If you pass in dictionary with multiple keys ... kwargs
        ''' Initialize topology and default options '''
        Topo.__init__(self, **opts)

        # add hosts
        host1 = self.addHost("User")
        host2 = self.addHost("Intermediary")
        host3 = self.addHost("Zoom")
        host4 = self.addHost("Skype")
        host5 = self.addHost("Email")
        host6 = self.addHost("Netflix")
        host7 = self.addHost("Hulu")

        # add switches
        switch1 = self.addSwitch("s1")
        switch2 = self.addSwitch("s2")
        switch3 = self.addSwitch("s3")
        switch4 = self.addSwitch("s4")
        switch5 = self.addSwitch("s5")
        switch6 = self.addSwitch("s6")
        switch7 = self.addSwitch("s7")

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
