#!/usr/bin/python
#
# quadrobot
# 8 DOF robot 
#
####################################################### 

import numpy as np
from math import sqrt, sin, cos, radians, pi, atan
from tools import get_random_item
from random import seed
import pygame as pg
from time import sleep

white = (250, 250, 250)
dark_grey = (100, 100, 100)
grey = (125, 125, 125)
light_grey = (150, 150, 150)
black = (0, 0, 0)


class Bot():
    def __init__(self, body_width=10, leg_len=6, height=2, strand=1):
        self.body = body_width
        self.L = leg_len
        self.heap_width = 9
        self.ankle_width = 7
        self.H = height
        self.S = strand
        self.scale = 15

        self.feet = np.ones(4, dtype=np.int)
        self.moves = np.array([
            [-1, -1, 1, 1],
            [4, 0, 0, 0],
            [0, 4, 0, 0],
            [0, 0, -4, 0],
            [0, 0, 0, -4]
        ])
        self.center = np.array([0, 0])
        self.path = []

        self.d_min = 1
        # self.d_max = sqrt(2*self.L**2 - self.H**2)
        self.d_max = self.d_min + 7


    def set_random_state(self):
        seed()
        Ls = range(2, 8)

        self.feet = np.array([
            get_random_item(Ls),
            get_random_item(Ls),
            get_random_item(Ls),
            get_random_item(Ls)
        ])


    def info(self):
        print "\nquadrobot info:\n" + "-" * 25
        print "  body size: (%i x %i)" % (self.body, self.body)
        print "  leg length: (%i + %i)" % (self.L, self.L)
        print "  feet range: (%i - %i)" % (int(self.d_min), int(self.d_max))
        print "  initial feet position:"
        # print "  fore left: %i  right: %i" % tuple(self.feet[:2])
        #print "  hind left: %i  right: %i" % tuple(self.feet[2:])
        print "-" * 25


    def is_legal(self, new_feet):
        return all([new_feet[i] <= self.d_max and new_feet[i] >= self.d_min for i in range(4)])


    def get_moveable_legs(self):
        legs = []
        if self.feet[0] > self.feet[3]:
            legs.append(1)
        elif self.feet[3] > self.feet[0]:
            legs.append(2)

        if self.feet[1] > self.feet[2]:
            legs.append(0)
        elif self.feet[2] > self.feet[1]:
            legs.append(3)

        return legs


    def take_action(self, action):
        """ returns True if suceesded. Otherwise returns False
		"""
        ## check if the leg can move
        # moveable_legs = range(4)
        moveable_legs = self.get_moveable_legs()
        if action != 0:
            if (action - 1) not in moveable_legs:
                self.path.append(20 + action)
                return False

        new_feet = self.feet + self.moves[action]
        if self.is_legal(new_feet):
            self.feet = new_feet
            self.path.append(action)
            return True
        else:
            self.path.append(10 + action)
            return False


    def get_state(self):
        """ returns an index which represents get_state
		"""
        return sum([(self.feet[i] - self.d_min) << 3 * i for i in range(4)])


    def draw_top_view(self, surf):
        (x0, y0) = (100, 100)
        radius = self.scale * self.body / 10

        surf.fill(black)
        rect = np.array([self.center[0] - self.body / 2, self.center[1] - self.body / 2, self.body, self.body])
        pg.draw.rect(surf, dark_grey, tuple(rect * self.scale + np.array([x0, y0, 0, 0])), 0)

        pos = np.array([self.center[0] + self.body / 2, self.center[1] + self.body / 2 + self.feet[0]])
        pg.draw.circle(surf, dark_grey, tuple(pos * self.scale + np.array([x0, y0])), radius, 0)

        pos = np.array([self.center[0] - self.body / 2, self.center[1] + self.body / 2 + self.feet[1]])
        pg.draw.circle(surf, dark_grey, tuple(pos * self.scale + np.array([x0, y0])), radius, 0)

        pos = np.array([self.center[0] + self.body / 2, self.center[1] - self.body / 2 - self.feet[2]])
        pg.draw.circle(surf, dark_grey, tuple(pos * self.scale + np.array([x0, y0])), radius, 0)

        pos = np.array([self.center[0] - self.body / 2, self.center[1] - self.body / 2 - self.feet[3]])
        pg.draw.circle(surf, dark_grey, tuple(pos * self.scale + np.array([x0, y0])), radius, 0)

        pg.display.flip()


    def draw_move_forward(self, prevCenter, surf, frames=5):
        for f in range(frames + 1):
            dc = self.scale * (self.center[1] - prevCenter) * (frames - f) / frames
            self.draw_bot(self.center[1] * self.scale - dc,
                          self.scale * self.feet - self.scale * self.moves[0] * (frames - f) / frames,
                          None,
                          None,
                          surf)
            pg.display.flip()
        # sleep(0.01)

    def draw_one_leg(self, raised_leg, prevFeet, surf, frames=11):
        for f in range(frames + 1):
            currFeet = self.scale * prevFeet + (self.feet - prevFeet) * self.scale * f / frames
            leg_height = 3 * f * (frames - f) * self.scale * self.H / frames ** 2

            self.draw_bot(self.scale * self.center[1],
                          currFeet,
                          raised_leg,
                          leg_height,
                          surf)
            pg.display.flip()
        # sleep(0.01)


    def draw_bot(self, center, feet, raised_leg, leg_height, surf):
        """draws in (y,z) axes. center and feet are given in pixels
		"""
        # print "Draw:", center, feet
        y0, z0 = 100, 300
        leg_z = np.array([3, 0, 3, 0])
        if raised_leg != None:
            leg_z[raised_leg] += leg_height

        surf.fill(black)

        fore_joint = (y0 + center + self.scale * self.body / 2, z0 - self.scale * self.H)
        hind_joint = (y0 + center - self.scale * self.body / 2, z0 - self.scale * self.H)

        ## draw left legs (0,2)
        theta0 = atan(feet[0] / self.H)
        theta2 = atan(feet[2] / self.H)

        L0 = sqrt(self.scale ** 2 * self.L ** 2 - self.scale ** 2 * self.H ** 2 / 4 - feet[0] ** 2 / 4)
        fore_knee0 = (y0 + center + self.scale * self.body / 2 + feet[0] / 2 + L0 * cos(theta0),
                      z0 - leg_z[0] - self.H / 2 - L0 * sin(theta0) )
        L2 = sqrt(self.scale ** 2 * self.L ** 2 - self.scale ** 2 * self.H ** 2 / 4 - feet[2] ** 2 / 4)
        hind_knee2 = (y0 + center - self.scale * self.body / 2 - feet[2] / 2 - L2 * cos(theta2),
                      z0 - leg_z[2] - self.H / 2 - L2 * sin(theta2) )

        pg.draw.line(surf, dark_grey, fore_joint, fore_knee0, self.heap_width)
        pg.draw.line(surf, dark_grey, fore_knee0, (y0 + center + feet[0] + self.scale * self.body / 2, z0 - leg_z[0]),
                     self.ankle_width)

        pg.draw.line(surf, dark_grey, hind_joint, hind_knee2, self.heap_width)
        pg.draw.line(surf, dark_grey, hind_knee2, (y0 + center - feet[2] - self.scale * self.body / 2, z0 - leg_z[2]),
                     self.ankle_width)

        ## draw body
        N = 20
        body = [(y0 + center + self.scale * self.body * cos(radians(180 * a / N)) / 2,
                 z0 - self.scale * self.H - self.body * sin(radians(180 * a / N)) * self.scale / 2)
                for a in range(N + 1)]

        pg.draw.polygon(surf, grey, body, 0)

        ## draw left legs (1,3)
        theta1 = atan(feet[1] / self.H)
        theta3 = atan(feet[3] / self.H)

        L1 = sqrt(self.scale ** 2 * self.L ** 2 - self.scale ** 2 * self.H ** 2 / 4 - feet[1] ** 2 / 4)
        fore_knee1 = (y0 + center + self.scale * self.body / 2 + feet[1] / 2 + L1 * cos(theta1),
                      z0 - leg_z[1] - self.H / 2 - L1 * sin(theta1) )
        L3 = sqrt(self.scale ** 2 * self.L ** 2 - self.scale ** 2 * self.H ** 2 / 4 - feet[3] ** 2 / 4)
        hind_knee3 = (y0 + center - self.scale * self.body / 2 - feet[3] / 2 - L3 * cos(theta3),
                      z0 - leg_z[3] - self.H / 2 - L3 * sin(theta3) )

        pg.draw.line(surf, light_grey, fore_joint, fore_knee1, self.heap_width)
        pg.draw.line(surf, light_grey, fore_knee1, (y0 + center + feet[1] + self.scale * self.body / 2, z0 - leg_z[1]),
                     self.ankle_width)

        pg.draw.line(surf, light_grey, hind_joint, hind_knee3, self.heap_width)
        pg.draw.line(surf, light_grey, hind_knee3, (y0 + center - feet[3] - self.scale * self.body / 2, z0 - leg_z[3]),
                     self.ankle_width)




