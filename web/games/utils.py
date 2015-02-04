#! /usr/bin/env python
# * coding: utf8 *

# Jack Says - A Web-Based, "Simon Says"-like, multiplayer game.
# Copyright (C) 2015  https://github.com/cedricbonhomme/JackSays
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

class Still(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "still"
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
        if username not in self.user_vals:
            self.user_vals[username]=0.0
        self.user_vals[username] += abs(data['ax'])+ abs(data['ay'])+abs(data['az'])
        return ""

    def finalize(self):
        #print self.user_vals.items()
        if len(self.user_vals)==0:
            return ""
        return [k for k,v in self.user_vals.items() if min(self.user_vals.values())==v][0]

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
        #print int(data["button"])==self.number

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
        #print self.user_vals.items()
        if len(self.user_vals)==0:
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
        if USERS != {}:
            return random.choice(USERS.keys())
        return ""

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
            #print self.count.most_common(2)
            return self.count.most_common(1)[0][0]
        return ""

class TSM(Game):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.game_id = "tsm"
        self.start_time= time.time()
        self.duration = 6
        self.data = {}
        self.start_script = "tsmStart"
        self.finish_script = "closeDialog"

        self.number = random.randint(1, 9)
        self.message = "Click on the number " + str(self.number)

    def get_data(self):
        #self.number = random.randint(4, 8)
        return str(self.number)

    def user_input(self, username, data):
        if username not in self.data and int(data["button"])==self.number:
            self.data[username] = time.time()
        #print int(data["button"])==self.number

    def finalize(self):
        if self.data.items() != []:
            result = reduce(lambda x,y: x if self.data[x]<=self.data[y] else y, self.data.iterkeys())
            return result
        return ""
