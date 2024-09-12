import argparse
from scapy.all import ARP, Ether, srp
import ipaddress

def print_banner():
    banner = """
    ##############################################################
    #                                                            #
    #              Welcome to the Python IP Scanner              #
    #              Scanning Your Network for Active Hosts         #
    #                                                            #
    ##############################################################
    """
    print(banner)

def arp_scan(network):
    # Print network being scanned
    print(f"[*] Scanning network: {network}")
    
    # Create a list of all IPs in the CIDR range
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(network).hosts()]

    # Create an ARP request and Ethernet broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = ARP(pdst=ip_list)
    packet = ether/arp

    # Send the packet and get the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Print out the active hosts
    print("[*] Active Hosts:")
    for sent, received in result:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

def main():
    # Print a big banner
    print_banner()

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Python IP Scanner Tool")
    parser.add_argument('--target', required=True, help="Target network in CIDR format (e.g., 192.168.1.0/24)")
    args = parser.parse_args()

    # Run the ARP scan on the provided target
    arp_scan(args.target)

if __name__ == "__main__":
    main()
