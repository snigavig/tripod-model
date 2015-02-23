#!/usr/bin/python
#
# quadrobot
# 8 DOF robot 
#
####################################################### 

import sys
from bot import Bot
from agent import Agent
from tools import read_data, write_data
import pygame as pg
import numpy as np
from time import sleep


white = (250,250,250)


def run(N):
	""" Runs N episodes of a given length and then runs a demo with greedy policy
	"""
	agent = Agent()

	data = read_data("data/q.dat")
	if data != None:
		agent.Q = data

	for i in range(N):
		bot = Bot()
		run_episode(bot,agent, None, draw=False, policy='eps_greedy')
		#if bot.center[1] > 7: print "quadrobot moved on: %i steps" % bot.center[1]



	_ = raw_input("Now see the demo. Press button to continue ...")
	pg.init()
	pg.display.init()
	surf = pg.display.set_mode((300,600))
	surf.fill(white)
	pg.display.flip()
	print "Surf1:", surf

	
	bot = Bot()
	bot.info()
	run_episode(bot,agent, surf, draw = True, policy='greedy', episode_len=60)
	print "Robot moves:\n", bot.path
	write_data(agent.Q,"data/q.dat")
	

def run_episode(bot, agent, surf, draw=False, policy='random', episode_len=20):
	bot.set_random_state()
	if draw: 
		print "Bot feet:",bot.feet
		
	for _ in range(episode_len):

		if policy == 'random':
			action = agent.get_random_policy()
		elif policy == 'greedy':
			action = agent.get_greedy_policy(bot.get_state())
		elif policy == 'eps_greedy':
			action = agent.get_policy(bot.get_state())
		else:
			print "Unknown policy:", policy
			raise

		prevState = bot.get_state()
		if not bot.take_action(action):
			reward = -5
		elif action == 0: # body move forward
			reward = 1
			bot.center += np.array([0,1])
		else:
			reward = 0

		agent.learn(prevState, bot.get_state(), action, reward)
		
		if draw: 
			bot.draw(surf)
			pg.display.flip()
			sleep(0.1)
			
			




if __name__ == '__main__':
	Args = sys.argv[:]
	if len(Args) !=2:
		print "Wrong syntax\nUSAGE: python run.py <nbr_training_episodes>"
	else:
		run( int(Args[1]) )

	
