#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arg():
    parser = optparse.OptionParser()
    parser.add_option('-i','--interface',dest='interface',help='Interface to change mac address')
    parser.add_option('-m','--mac',dest='new_mac',help='New mac address')
    (options,arguments) = parser.parse_args()    

    if not options.interface:
        parser.error('[+] Please specify an interface, use --help for mor info')
    elif not options.new_mac:
        parser.error('[+] Please specify a new mac address, use --help for mor info')

    return options
     

def mac_changer(interface,new_mac):
    subprocess.call(['ifconfig', interface ,'down'])
    print('[+] eth0 is down')

    subprocess.call(['ifconfig', interface , 'hw' ,'ether', new_mac ])
    print('[+] eth0 mac address is changed')

    subprocess.call(['ifconfig', interface ,'up'])
    print('[+] eth0 is up')

options = get_arg()
#mac_changer(options.interface,options.new_mac)

ifconfig_results = subprocess.check_output(['ifconfig',options.interface])
print(ifconfig_results)

mac_address_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',ifconfig_results)

if mac_address_result:
    print(mac_address_result.group(0))

else:
    print('[-] Could not find mac address')