#!/usr/bin/python
#
# quadrobot
# 8 DOF robot 
#
####################################################### 

import numpy as np
from math import sqrt, sin, cos
from tools import get_random_item
from random import seed



class Bot():
	def __init__(self, body_width=3, leg_len=5, height=2, strand=1):
		self.body = body_width
		self.L = leg_len
		self.H = height
		self.S = strand
		self.feet = np.zeros(4,dtype=np.int)
		self.moves = np.array([
			[-1,-1,-1,-1],
			[ 4, 0, 0, 0],
			[ 0, 4, 0, 0],
			[ 0, 0, 4, 0],
			[ 0, 0, 0, 4]
			])
		self.center = 0
		self.path = []

		self.d_min = 0
		self.d_max = sqrt(2*self.L**2 - self.H**2)


	def set_random_state(self):
		seed()
		Ls = range(8)

		self.feet = np.array([
			get_random_item(Ls),
			get_random_item(Ls),
			get_random_item(Ls),
			get_random_item(Ls)
			])



	def info(self):
		print "\nquadrobot info:\n"+"-"*25
		print "  body size: (%i x %i)" %(self.body, self.body)
		print "  leg length: (%i + %i)" % (self.L,self.L)
		print "  initial feet position:"
		print "  fore left: %i  right: %i" % tuple(self.feet[:2])
		print "  hind left: %i  right: %i" % tuple(self.feet[2:])
		print "-"*25



	def is_legal(self, new_feet):
		return all([ new_feet[i]<=self.d_max and new_feet[i]>= self.d_min for i in range(4)])


	def take_action(self, action):
		""" returns True if suceesded. Otherwise returns False
		"""
		new_feet = self.feet + self.moves[action]
		if self.is_legal(new_feet):
			self.feet = new_feet
			self.path.append(action)
			return True
		else:
			self.path.append(-action)
			return False


	def get_state(self):
		""" returns an index which represents get_state
		"""
		return sum([ self.feet[i]<<3*i for i in range(4)])








