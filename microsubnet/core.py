import ipaddress

def calculate(cidr):

    print()
    print("MicroSubnet")
    print("=" * 40)

    network = ipaddress.ip_network(cidr, strict=False)

    print("CIDR      :", cidr)
    print("Network   :", network.network_address)
    print("Broadcast :", network.broadcast_address)
    print("Netmask   :", network.netmask)
    print("Hosts     :", network.num_addresses)
    print("First IP  :", list(network.hosts())[0])
    print("Last IP   :", list(network.hosts())[-1])
