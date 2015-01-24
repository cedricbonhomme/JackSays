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
        self.param = None
    def get_data(self):
        return self.duration
    def user_input(self, username, param):
        pass
    def finalize(self):
        pass

class PickOne (Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "pickone"
        self.start_time= time.time()
        self.duration = 60
        self.param = None
    def get_data(self):
        return self.duration
    def user_input(self, username, param):
        pass
    def finalize(self):
        pass
