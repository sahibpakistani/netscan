#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_mac = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast_mac = broadcast_mac/arp_request
    print(arp_request_broadcast_mac.summary())
    answered_list = scapy.srp(arp_request_broadcast_mac, timeout=1, verbose=False) [0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return (client_list)


def print_result (result_list):
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


ip = raw_input("Enter IP to scan >")
scan_result = scan(ip)
print_result(scan_result)
print ("Made By S.M Proud to be a Muslim")
