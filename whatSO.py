#!/usr/bin/python3
#coding: utf-8
import re, sys, subprocess

#python3 whats.py <ip victima>

if len(sys.argv) != 2:
	print("[*] USE: python3  " + sys.argv[0] + " <ip victima>")
	sys.exit(1)

def get_ttl(ip_add):
	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_add, ""], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()

	out = out.split()
	out = out[12].decode('utf-8')

	ttl_value = re.findall(r"\d{1,3}", out)[0]
	return ttl_value
def get_os(ttl):
	
	ttl= int(ttl)
	if ttl >= 0 and ttl <= 64:
		return "Linux"
	elif ttl >= 65 and ttl <=128:
		return "Windows"
	else:
		return "NOT FOUND"

if __name__=='__main__':
	ip_add = sys.argv[1]
	ttl = get_ttl(ip_add)
	
	os_name = get_os(ttl)
	print("%s (ttl -> %s): %s" % (ip_add, ttl, os_name))
