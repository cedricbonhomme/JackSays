#! /usr/bin/env python
# -*- coding: utf-8 -*-
from web.models import Game
import time

class WaitGame (Game):
    def __init__(self):
        self.game_id = "wait"
        self.start_time= time.time()
        self.duration = 10
    def get_data():
        return None
    def user_input(self, username, param):
        pass
    def finalize(self):
        pass
