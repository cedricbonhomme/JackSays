#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
from web.models import Game
from web import USERS

class WaitGame(Game):
    """
    Used for waiting before the first game starts.
    """
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "wait"
        self.start_time= time.time()
        self.duration = 30
        self.data = None
        self.message = "Hang on..."

    def get_data(self):
        return self.duration

    def user_input(self, username, data):
        pass

    def finalize(self):
        return ""

#
# Games definition
#

class PickOne(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "pickone"
        self.start_time= time.time()
        self.duration = 10
        self.data = {}

    def get_data(self):
        return self.duration

    def user_input(self, username, data):
        if username not in self.data:
            self.data[username] = time.time()

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())

class Roma(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "roma"
        self.start_time= time.time()
        self.duration = 6
        self.data = {}

        self.number = random.randint(4, 8)
        self.message = "Click on the number " + str(self.number)

    def get_data(self):
        #self.number = random.randint(4, 8)
        return "Click on the number " + str(self.number)

    def user_input(self, username, data):
        if username not in self.data and int(data["button"])==self.number:
            self.data[username] = time.time()
        print int(data["button"])==self.number

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())
            return result
        return ""

class Sound(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "sound"
        self.start_time= time.time()
        self.duration = 10
        self.data = {}
        self.message = ""

    def get_data(self):
        return self.duration

    def user_input(self, username, data):
        if username not in self.data:
            self.data[username] = time.time()

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())

class Shake(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "shake"
        self.start_time= time.time()
        self.duration = 10
        self.data = {}
        self.message = "Get ready to..."
        self.start_script = "accelerometer_data_deamon_start"
        self.finish_script = "accelerometer_data_deamon_stop"
        self.user_vals={}

    def get_data(self):
        return "Get ready to..."

    def user_input(self, username, data):
        print username,data
        if username not in self.user_vals:
            self.user_vals[username]=0.0    
        self.user_vals[username] += abs(data['ax'])+ abs(data['ay'])+abs(data['az'])
        return ""

    def finalize(self):
        print self.user_vals.items()
        if len(self.user_vals)=0:
            return ""
        return [k for k,v in self.user_vals.items() if max(self.user_vals.values())==v][0]

        #return self.user_vals #random.choice(USERS.keys())

class Scream(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "scream"
        self.start_time= time.time()
        self.duration = 5
        self.data = {}
        self.message = "Get ready to..."

    def get_data(self):
        return "Get ready to..."

    def user_input(self, username, data):
        return ""

    def finalize(self):
        return random.choice(USERS.keys())

from collections import Counter
class Click(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "clicke"
        self.start_time= time.time()
        self.duration = 5
        self.data = {}
        self.message = "Click click click!"
        self.count = Counter()

    def get_data(self):
        return "Click click click!"

    def user_input(self, username, data):
        self.count[username] += 1

    def finalize(self):
        if self.count.most_common() != []:
            print self.count.most_common(2)
            return self.count.most_common(1)[0][0]
        return ""
