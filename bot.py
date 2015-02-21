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
import pygame as pg



class Bot():
	def __init__(self, body_width=10, leg_len=20, height=2, strand=1):
		self.body = body_width
		self.L = leg_len
		self.H = height
		self.S = strand
		self.feet = np.zeros(4,dtype=np.int)
		self.moves = np.array([
			[-1,-1,1,1],
			[ 4, 0, 0, 0],
			[ 0, 4, 0, 0],
			[ 0, 0,-4, 0],
			[ 0, 0, 0,-4]
			])
		self.center = np.array([0,0])
		self.path = []

		self.d_min = 0
		#self.d_max = sqrt(2*self.L**2 - self.H**2)
		self.d_max = 7


	def set_random_state(self):
		seed()
		Ls = range(7)

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
		print "  feet range: (%i - %i)" % (int(self.d_min),int(self.d_max))
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
			self.path.append(10+action)
			return False


	def get_state(self):
		""" returns an index which represents get_state
		"""
		return sum([ self.feet[i]<<3*i for i in range(4)])


	def draw(self, surf):
		white = (250,250,250)
		dark_grey = (50,50,50)
		(x0,y0) = (100,100)
		scale = 10
		radius = scale * self.body / 10
		
		surf.fill(white)
		rect = np.array([self.center[0]-self.body/2, self.center[1]-self.body/2, self.body, self.body])
		pg.draw.rect(surf, dark_grey, tuple( rect*scale+np.array([x0,y0,0,0]) ),0)
		
		pos = np.array([self.center[0]+self.body/2, self.center[1]+self.body/2+self.feet[0]])
		pg.draw.circle(surf, dark_grey, tuple( pos*scale+np.array([x0,y0]) ), radius, 0)

		pos = np.array([self.center[0]-self.body/2, self.center[1]+self.body/2+self.feet[1]])
		pg.draw.circle(surf, dark_grey, tuple( pos*scale+np.array([x0,y0]) ), radius, 0)

		pos = np.array([self.center[0]+self.body/2, self.center[1]-self.body/2-self.feet[2]])
		pg.draw.circle(surf, dark_grey, tuple( pos*scale+np.array([x0,y0]) ), radius, 0)

		pos = np.array([self.center[0]-self.body/2, self.center[1]-self.body/2-self.feet[3]])
		pg.draw.circle(surf, dark_grey, tuple( pos*scale+np.array([x0,y0]) ), radius, 0)



