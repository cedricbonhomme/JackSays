#! /usr/bin/env python
# -*- coding: utf-8 -*-

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
from flask.ext.login import UserMixin

class User(UserMixin):
    """
    Represent a user.
    """
    def __init__(self, nic, score, avatar = "M123"):
        self.nic = nic
        self.score = score
        self.avatar = avatar

    def get_id(self):
        """
        Return the id of the user.
        """
        return self.nic

    def dump(self):
        return {"nic": self.nic,
                "score": self.score}

class Game(object):
    """
    Represent a mini game.
    """
    def __init__(self):
        self.user_vals = {}
        self.game_id = 0
        self.duration = 30.0
        self.data = None
        self.stime = time.time()
        self.message = ""
        self.start_script = ""
        self.finish_script = ""

    def get_time_left(self):
        return self.duration-(time.time()-self.stime)

    def get_data(self):
        return None

    def user_input(self, username, data):
        self.user_vals[username] = data

    def finalize(self):
        """
        overload this method
        """
        return ""
