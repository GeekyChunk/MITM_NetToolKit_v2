from scapy.all import *

face = raw_input('Enter Your Interface Name: ')
N = input('number of packet: ')

def packet(p):

    print p.summary()
    print
    return



sniff(iface=face,count=100,prn=packet)
