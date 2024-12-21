
#!/usr/bin/python

# Modulos de Mininet importados

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

# Clase para crear la red

class MyTopo(Topo):
    def build(self):

        # Creando router
        r1 = self.addHost('r1', ip='10.8.0.1/28')

        # Creando 3 hosts
        h1 = self.addHost('h1', ip='10.8.0.2/28')
        h2 = self.addHost('h2', ip='10.8.0.3/28')
        h3 = self.addHost('h3', ip='10.8.0.4/28')
        h4 = self.addHost('h4', ip='10.8.0.5/28')

        # Enlaces entre el router y los hosts
        self.addLink(r1, h1)
        self.addLink(r1, h2)
        self.addLink(r1, h3)
        self.addLink(r1, h4)
        
# Iniciando la red

def run():
    setLogLevel('info')  # Estableciendo el nivel de log a info
    topo = MyTopo()       # Creando la topología
    net = Mininet(topo=topo, switch=OVSKernelSwitch)
    net.start()          # Iniciando la red

    for i in range(1, 5):
        host = net.get(f'h{i}')

    # Iniciando la CLI de Mininet
    CLI(net)

    # Deteniendo la red al salir de la CLI
    net.stop()

if __name__ == '__main__':
    run()