import os
CMD_1st = "clear"
os.system(CMD_1st)
print "\n"
print "\t+-------------------------------------------------------+"
print "\t|  NET_TollKit by MITM                                  |"
print "\t+---------------------------+---------------------------+"
print "\t|      o O o                |                           |"
print '\t|              o O          | |""""""""""""|======[***  |'
print "\t|                 o         | |  WIFIKILL  \            |"
print "\t| |^^^^^^^^^^^^^^|l___      | |_____________\_______    |"
print '\t| |    SNIFFING    |""\___, | |==[MITM>]============\   |'
print "\t| |________________|__|)__| | |______________________\  |"
print '\t| |(@)(@)"""**|(@)(@)**|(@) | \(@)(@)(@)(@)(@)(@)(@)/   |'
print "\t|  = = = = = = = = = = = =  |  *********************    |"
print "\t+---------------------------+---------------------------+"
print "\n\tChoose the number of your service:"
print "\t0) setup\n\t1) Net analyze\n\t2) interface sniff\n\t3) site info\n\t4) wifi killer\n\t99) exit(if dosent close use it again)\n\n"
SRV = []
service = raw_input('service: ')
SRV.append(service)
if "99" in SRV:
    exit()
else:
	print
if "0" in SRV:
    import os
    CMD_1st = "python files/setup.py"
    clear = "clear"
    os.system(clear)
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "1" in SRV:
    import os
    CMD_1st = "python files/Clients.py"
    clear = "clear"
    os.system(clear)
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "2" in SRV:
    import os
    CMD_1st = "sudo python files/sniff.py"
    clear = "clear"
    os.system(clear)
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "3" in SRV:
    import os
    CMD_1st = "python files/info_site.py"
    clear = "clear"
    os.system(clear)
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "4" in SRV:
    import os
    CMD_1st = "sudo python files/WiFi_Killer.py"
    clear = "clear"
    os.system(clear)
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    import os
    CMD_1st = "clear"
    CMD_2nd = "python NET_Tool.py"
    os.system(CMD_1st)
if "99" in SRV:
    exit()
else:
	print
CMD_RE = "python NET_ToolKit.py"
os.system(CMD_RE)
