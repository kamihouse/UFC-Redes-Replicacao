from threading import Thread
from time import sleep

class Th(Thread):

	def __init__ (self, delay):
		Thread.__init__(self)
		self.delay = delay

	def run(self):
		for x in xrange(10):
			print x
			sleep(self.delay)

a = Th(3)
a.start()