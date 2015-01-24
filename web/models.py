#! /usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):
    """
    Represent a user.
    """
    def __init__(self, nic, score):
        self.nic = nic
        self.score = score

    def dump(self):
        return {"nic": self.nic,
                "score": self.score}

class Game(object):
    """
    Represent a mini game
    """
    def __init__(self):
        self.user_vals = {}
    def user_input(self, username, param):
        self.user[username] = param
    def finalize(self):
        """
        overload this method
        """
        pass
