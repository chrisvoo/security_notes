import subprocess 
from colors import Print
import re

class Ping:
	"""It wraps ping tool"""
	requests = 4   				# Stop after sending count ECHO_REQUEST packets 
	target = ""					# target host, last parameter
	quiet = True				# Quiet output.  Nothing is displayed except the summary lines  at  startup  time and when finished.
	packetSize = 56				# Specifies the number of data bytes to be sent.
	rawOutput = ""
	stats = { 
		"transmitted" : 0,
		"received": 0,
		"packet_loss": 0,
		"total_time": 0
	}
	
	def __init__(self, host):
		self.target = host
	
	def withRequest(self, num):
		self.requests = int(num)
		return self
		
	def withQuiet(self, q):
		self.quiet = q
		return self
		
	def withPacketSize(self, pSize):
		self.packetSize = int(pSize)
		return self		
		
	def getStats(self):
		return self.stats
		
	def isTargetReachable(self):
		""" A target is considered not reachable if every packet is lost """
		if self.stats is not None:
			return self.stats["packet_loss"] != 100
		else:
			return False
		
	def execute(self):
		""" Executes ping command, if everything's ok returns True, otherwise False """
		try:
			command = "ping "
			command += "-c " + str(self.requests) + " "
			command += ("-q" if self.quiet else "") + " "
			command += "-s " + str(self.packetSize) + " "	
			command += self.target
			
			self.rawOutput = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
			stats = re.compile("\d+")
			
			for line in self.rawOutput:		
				if line.find("transmitted") != -1:
					digitList = stats.findall(line)
					for i, val in enumerate(digitList):
						if i == 0:
							stats["transmitted"] = val
						elif i == 1:
							stats["received"] = val
						elif i == 2:
							stats["packet_loss"] = val
						elif i == 3:
							stats["total_time"] = val
		
			return True
		except subprocess.CalledProcessError as e:
			if e.output.find("100% packet loss") == -1:
				# an exception occurred
				Print.error("Error for " + e.cmd + "\n" + e.output)
				return False
			else:
				# host not reachable
				self.stats["packet_loss"] = 100
				return True
