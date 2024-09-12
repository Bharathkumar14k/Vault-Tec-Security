# Vault-Tec-Security
 Internship - Project
# Python IP Scanner Tool

## Overview

This Python tool performs network scanning using ARP (Address Resolution Protocol) to identify active hosts on a network. It provides an easy way to discover devices on a specified network range and display their IP and MAC addresses.

## Features

- Scans a network range using ARP requests.
- Displays active hosts with their IP and MAC addresses.
- Command-line interface with support for specifying the target network.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Bharathkumar14k/Vault-Tec-Security.git
   cd Vault-Tec-Security
 ##Install dependencies:
 pip install scapy

##Run
python3 scan.py --target 192.168.1.0/24

##Output:

##############################################################
#                                                            #
#              Welcome to the Python IP Scanner              #
#              Scanning Your Network for Active Hosts         #
#                                                            #
##############################################################

[*] Scanning network: 192.168.1.0/24
[*] Active Hosts:
IP: 192.168.1.2, MAC: aa:bb:cc:dd:ee:ff
IP: 192.168.1.5, MAC: 11:22:33:44:55:66

