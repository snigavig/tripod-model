#!/usr/bin/python
#
# quadrobot
# 8 DOF robot 
#
####################################################### 

from tools import coin, get_random_item
import numpy as np


class Agent():
	def __init__(self, eps=0.1, alpha=0.3, gama=0.9):
		self.eps = eps
		self.alpha = alpha
		self.gama = gama

		self.Q = np.zeros((4096,5))
		self.Q_values = []


	def get_policy(self, state):
		return self.get_eps_policy(state)

	def get_random_policy(self):
		return get_random_item(range(5))

	
	def explore_alternative_actions(self, state):
		Qa_values = self.Q[state]
		Vmax = Qa_values.max()
		alternative_actions = [ i for i in range(5) if Qa_values[i] >= Vmax / 2 ]
		if len(alternative_actions) != 0:
			return get_random_item(alternative_actions)
		else:
			return Qa_values.argmax()



	def get_eps_policy(self, state):
		if coin(self.eps):
			return self.explore_alternative_actions(state)
		else:
			return self.get_greedy_policy(state)


	def get_greedy_policy(self, state):
		assert state < 4096

		Qa_values = self.Q[state]
		Vmax = Qa_values.max()
		indices = [ i for i in range(5) if Qa_values[i]==Vmax]
		
		return get_random_item(indices)


	def get_state_value(self, state):
		return self.Q[ state ].max()


	def learn(self, state, nextState, action, reward):
		V1 = self.get_state_value(nextState)
		V = self.Q[(state,action)]
		
		V_new = V + self.alpha * (reward + self.gama * V1 - V)
		self.Q[ ( state,action) ] = V_new
		
		