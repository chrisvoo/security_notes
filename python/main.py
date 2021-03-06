#!/usr/bin/python

import sys, getopt
import socket
from ping import Ping
from which import Which
from colors import Print

def main(argv):
   target = ''
   
   try:
      opts, args = getopt.getopt(argv,"ht:o:l",["target=", "list"])
   except getopt.GetoptError:
      Print.error('Unknown option: main.py -t <target>')
      sys.exit(2)
      
   if len(opts) == 0:
     Print.error('No arguments passed! Usage: main.py -t <target>')
     sys.exit(2)
      
   for opt, arg in opts:
      if opt == '-h':
         print 'Help: main.py -t <target>'
         sys.exit()
      elif opt in ("-t", "--target"):
		 try:
			target = socket.gethostbyname(arg)
		 except socket.error, e1:
			Print.error(arg + ": " + str(e1))
			sys.exit(2)
      elif opt in ("-l", "--list"):
		  print "Tools list:"
		  Print.conditional("Ping", Which.exists("ping"))
		  sys.exit(0)
		  
		           
   print 'Target: ' + Print.bold(target, True)
   ping = Ping(target).withRequest(1)
   if ping.execute() and ping.isTargetReachable():
	   Print.success("Host reachable with ICMP") 
   else:
	   Print.error("Host not reachable")
   

if __name__ == "__main__":
   main(sys.argv[1:])
