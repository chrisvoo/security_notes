import subprocess 
from colors import Print

class Which:
  """ Wrapper for which command, used to see if a tool is installed and present in $PATH """
  @staticmethod
  def getHome(cmd):
	  try:
		return subprocess.check_output(
			"which " + cmd, 
			stderr=subprocess.STDOUT, 
			shell=True).rstrip()
	  except subprocess.CalledProcessError as e:
		Print.error("Error for " + e.cmd + "\n" + e.output)
		return None

  @staticmethod
  def exists(cmd):
	  return Which.getHome(cmd) is not None
