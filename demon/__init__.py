"""
Overlaying module to the daemonize module to add more features.
Subclass the demon class and implement the daemonize() function that is called to run in the background.
Then instantiate your subclass passing it the PID file path
"""

import os
import signal
import time

import daemonize

class demon:
	def __init__(self, appname, pidf, action, args=None):
		self.appname = appname
		self.pidf = pidf
		self.daemonize_args = args

		if action == 'start':
			self.start()
		elif action == 'stop':
			self.stop()
		elif action =='restart':
			self.restart()
		elif action == 'status':
			self.status()
		elif action == 'fg':
			self.fg()
		else:
			raise ValueError("Unrecognized daemonize action: '%s' (start, stop, restart, status, fg)" % action)

	def start(self):
		print("Daemonizing")
		d = daemonize.Daemonize(app=self.appname, pid=self.pidf, action=self.daemonize, privileged_action=lambda: self.daemonize_args)
		d.start()

	def fg(self):
		self.daemonize(*self.daemonize_args)

	def stop(self):
		if not os.path.exists(self.pidf):
			print("%s daemon not running" % self.appname)
			sys.exit(-1)

		with open(self.pidf, 'r') as f:
			p = f.read()
			p = int(p)
		print("Stopping daemon PID %d" % p)
		os.kill(p, signal.SIGTERM)

	def restart(self, pause=1.0):
		self.stop()
		# For good measure if needed
		if pause > 0:
			time.sleep(pause)
		self.start()

	def status(self):
		if not os.path.exists(self.pidf):
			print("%s: Stopped" % self.appname)
			sys.exit(0)

		with open(self.pidf, 'r') as f:
			p = f.read()
			p = int(p)
		print("%s: Running (PID %d)" % (self.appname, p))

	def daemonize(self, *args):
		raise NotImplementedError("Must implement daemonize function to actually run your process")

