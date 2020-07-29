port1 = {21:"FTP", 22:"SSH",23:"telnet",80:"http"}
for k in list(port1.keys()):
       port1[port1.pop(k)] = k

port1