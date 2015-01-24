#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.login import UserMixin

class User(UserMixin):
    """
    Represent a user.
    """
    def __init__(self, nic, score):
        self.nic = nic
        self.score = score

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

    def user_input(self, username, param):
        self.user[username] = param

    def finalize(self):
        """
        overload this method
        """
        pass
