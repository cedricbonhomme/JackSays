#! /usr/bin/env python
# -*- coding: utf-8 -*-
from web.models import Game
import time

class Game1 (Game):
    def __init__(self):
        self.game_id = 0
        self.start_time= time.time()
    def user_input(self, username, param):
        self.user[username] = time.time()-start_time
        print self.user
    def finalize(self):
        pass
