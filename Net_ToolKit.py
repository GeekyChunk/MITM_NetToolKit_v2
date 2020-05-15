import os
CMD_1st = "clear"
os.system(CMD_1st)
print "Wellcome Dear\nChoose the number of your service"
print
print
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
    os.system(CMD_1st)
else:
    print
if "1" in SRV:
    import os
    CMD_1st = "python files/Clients.py"
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "2" in SRV:
    import os
    CMD_1st = "sudo python files/sniff.py"
    os.system(CMD_1st)
else:
    print
if "3" in SRV:
    import os
    CMD_1st = "python files/info_site.py"
    os.system(CMD_1st)
    exit = raw_input('Press Enter for close')
else:
    print
if "4" in SRV:
    import os
    CMD_1st = "sudo python files/WiFi_Killer.py"
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
CMD_RE = "python NET_Tool.py"
os.system(CMD_RE)
