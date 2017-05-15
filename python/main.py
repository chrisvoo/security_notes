#!/usr/bin/python

import sys, getopt
import socket

def main(argv):
   target = ''
   
   try:
      opts, args = getopt.getopt(argv,"ht:o:",["target="])
   except getopt.GetoptError:
      print 'main.py -t <target>'
      sys.exit(2)
      
   if len(opts) == 0:
     print 'main.py -t <target>'
     sys.exit()
      
   for opt, arg in opts:
      if opt == '-h':
         print 'main.py -t <target>'
         sys.exit()
      elif opt in ("-t", "--target"):
		 try:
			target = socket.gethostbyname(arg)
		 except socket.error, e:
			print arg + ": " + str(e); 
			sys.exit()
			
         
   print 'Target: ', target

if __name__ == "__main__":
   main(sys.argv[1:])
