from scapy.all import *
import random
import sys
from scapy.base_classes import Gen, Net, SetGen

def send_p(src_ip,data):
    Source_IP= src_ip
    #Dest_ip = '192.168.11.52'
    Dest_ip = '192.168.1.30'
    Src_Port = random.randint(5000,7000)
    pyload = data
    spoofed_packet = fragment(IP(src=Source_IP, dst=Dest_ip) / UDP(sport=Src_Port, dport=514) / Raw(pyload),65535)
    send(spoofed_packet)

SIP = sys.argv[1]
fpath = sys.argv[2]
f=open (fpath, "rb") #Input Filename
for val in f.readlines():
	send_p(SIP,val)
  	val=None
f.close()
