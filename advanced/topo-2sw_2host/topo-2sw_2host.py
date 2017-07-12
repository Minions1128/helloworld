"""
	Custom topology example
	Two directly connected swtiches plus two hosts for each switch:
		host1 --- switch1 --- switch2 --- host3
			     |		 |
			     |		 |
			   host2       host4
"""
from mininet.topo import Topo

class my_topo(Topo):
	"Simple topology example."

	def __init__(self):
		"Create custom topo."

		# Initialize topology
		Topo.__init__(self)

		# Add hosts and switches
		Host1 = self.addHost('h1')
		Host2 = self.addHost('h2')
		Host3 = self.addHost('h3')
		Host4 = self.addHost('h4')
		Switch1 = self.addSwitch('s1')
		Switch2 = self.addSwitch('s2')

		# Add links
		self.addLink(Host1, Switch1)
		self.addLink(Host2, Switch1)
		self.addLink(Switch2, Host3)
		self.addLink(Switch2, Host4)
		self.addLink(Switch1, Switch2)

topos = {'mytopo':(lambda:my_topo())}
