from helpers import consoleHelper
from constants import bcolors

class invalidArgumentsException(Exception):
	def __init__(self, handler):
		consoleHelper.printColored("[{}] Invalid arguments".format(handler), bcolors.RED)

class loginFailedException(Exception):
	def __init__(self, handler, who):
		consoleHelper.printColored("[{}] {}'s Login failed".format(handler, who), bcolors.RED)

class userBannedException(Exception):
	def __init__(self, handler, who):
		consoleHelper.printColored("[{}] {} is banned".format(handler, who), bcolors.RED)

class osuApiFailException(Exception):
	def __init__(self, handler):
		consoleHelper.printColored("[{}] Invalid data from osu!api".format(handler), bcolors.RED)

class fileNotFoundException(Exception):
	def __init__(self, handler, file):
		consoleHelper.printColored("[{}] File not found ({})".format(handler, file), bcolors.RED)

class invalidBeatmapException(Exception):
	pass

class beatmapTooLongException(Exception):
	def __init__(self, handler):
		consoleHelper.printColored("[{}] Requested beatmap is too long.".format(handler), bcolors.RED)
