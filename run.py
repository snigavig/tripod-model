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



	pg.init()
	pg.display.init()
	surf = pg.display.set_mode((800,600))
	surf.fill((0,0,0))
	pg.display.flip()
	print "Surf1:", surf

	
	bot = Bot()
	bot.info()
	run_episode(bot,agent, surf, draw = True, policy='eps_greedy', episode_len=80)
	print "Robot's last 20 moves:\n", bot.path[-20:]
	print "Robot walked %i m" % bot.center[1]
	print "Last state value=%.1f" % agent.get_state_value(bot.get_state()) 
	write_data(agent.Q,"data/q.dat")
	#_ = raw_input("Press ENTER to quit ...")
	
	

def run_episode(bot, agent, surf, draw=False, policy='random', episode_len=20):
	bot.set_random_state()
	if draw: 
		print "Robot's starting state:",bot.feet
		
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
		prevFeet = bot.feet.copy()
		prevCenter = bot.center[1]
	
		if not bot.take_action(action):
			reward = -5

		elif action == 0: # body move forward
			reward = 1
			bot.center += np.array([0,1])
			if draw: bot.draw_move_forward(prevCenter, surf)
			
		else:
			reward = 0
			leg = action - 1
			if draw: bot.draw_one_leg(leg, prevFeet, surf)
			

		agent.learn(prevState, bot.get_state(), action, reward)
				
			




if __name__ == '__main__':
	Args = sys.argv[:]
	if len(Args) !=2:
		print "Wrong syntax\nUSAGE: python run.py <nbr_training_episodes>"
	else:
		run( int(Args[1]) )

	
