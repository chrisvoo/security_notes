
class Print:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def conditional(msg, result, ret=None):
		"""
		Prints or returns a red error message or a green success message based on a condition
		Keyword arguments:
		msg: the message
		result: the condition
		ret: boolean, if true returns the string instead of printing it
		"""		
		m = Print.success(msg, True) if result else Print.error(msg, True)
		if ret: 
			return m
		else:
			print m

    @staticmethod
    def error(msg, ret=None):
		"""
		Prints or returns a red error message
		Keyword arguments:
		msg: the message
		ret: boolean, if true returns the string instead of printing it
		"""
		m = Print.FAIL + msg + Print.ENDC
		if ret: 
			return m
		else:
			print m

    @staticmethod
    def warn(msg, ret=None):
		"""
		Prints or returns a yellow warning message
		Keyword arguments:
		msg: the message
		ret: boolean, if true returns the string instead of printing it
		"""		
		m = Print.WARNING + msg + Print.ENDC
		if ret: 
			return m
		else:
			print m		

    @staticmethod
    def success(msg, ret=None):
		"""
		Prints or returns a green success message
		Keyword arguments:
		msg: the message
		ret: boolean, if true returns the string instead of printing it
		"""				
		m = Print.OKGREEN + msg + Print.ENDC
		if ret: 
			return m
		else:
			print m
		
    @staticmethod
    def bold(msg, ret=None):
		"""
		Prints or returns a bold message
		Keyword arguments:
		msg: the message
		ret: boolean, if true returns the string instead of printing it
		"""				
		m = Print.BOLD + msg + Print.ENDC	
		if ret: 
			return m
		else:
			print m
