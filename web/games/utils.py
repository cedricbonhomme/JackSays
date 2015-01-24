#! /usr/bin/env python
# -*- coding: utf-8 -*-
from web.models import Game
import time



class WaitGame (Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "wait"
        self.start_time= time.time()
        self.duration = 60
        self.data = None
    def get_data(self):
        return self.duration
    def user_input(self, username, data):
        pass
    def finalize(self):
        pass

class PickOne (Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "pickone"
        self.start_time= time.time()
        self.duration = 10
        self.data = {}

    def get_data(self):
        return self.duration

    def user_input(self, username, data):
        if username in self.data:
            self.data[username] = time.time()

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())
            print result
