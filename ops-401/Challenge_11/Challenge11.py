#!/usr/bin/env python3

# Script name Challenge: 401 Challenge 11
# Author Name Christen Reinhart
# Date of Latest Revision 01/22/2024
# Sources https://chat.openai.com/share/ee10763b-db45-4241-a631-97da167ec5a9 
# Purpose In Python, Create a TCP Port Range Scanner  

from scapy.all import Ether, IP, sniff

my_frame = Ether() / IP()

print(my_frame)
print('-' * 80)
print(my_frame.show())
# print(my_frame.summary())
print('-' * 80)

packets = sniff(count=10)




