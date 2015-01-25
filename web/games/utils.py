#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
from web.models import Game

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
        self.duration = 4
        self.data = {}

        self.number = random.randint(4, 8)

    def get_data(self):
        self.number = random.randint(4, 8)
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

    def get_data(self):
        return self.duration

    def user_input(self, username, data):
        if username not in self.data:
            self.data[username] = time.time()

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())
