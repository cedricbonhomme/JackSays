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