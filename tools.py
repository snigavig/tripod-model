#!/usr/bin/python
#
# quadrobot
# 8 DOF robot 
#
####################################################### 

from random import random
import os
import pickle


def coin(p): return p > random()


def get_random_item(Ls):
    return Ls[int(random() * len(Ls))]


def read_data(my_file):
    if not os.path.isfile(my_file):
        return None

    with open(my_file, 'rb') as handle:
        data = pickle.loads(handle.read())
    handle.close()

    return data


def write_data(data, my_file):
    with open(my_file, 'wb') as handle:
        pickle.dump(data, handle)
    handle.close()


def write_path(Q_values, my_file):
    with open(my_file, 'w') as handle:
        for val in Q_values:
            line = str(val[0]) + ', ' + \
                   str(val[1]) + ', ' + \
                   str(val[2]) + ', ' + \
                   str(val[3]) + ', ' + \
                   str(val[4]) + '\n'
            handle.write(line)

    handle.close()

	
