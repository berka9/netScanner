import scapy.all as scapy
import optparse

def get_user_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i","--ipaddress", dest="ip_address",help="Enter Ip Address")

    (user_input, arguments) = parse_obj.parse_args()
    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input
def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = broadcast/arp_request
    (answered_list, unanswered_list) = scapy.srp(combined,timeout=1)
    answered_list.summary()

user_ip_address = get_user_input()
scan_network(user_ip_address.ip_address)