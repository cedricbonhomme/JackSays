#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from flask import Flask
from flask.ext.socketio import SocketIO

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None

USERS = []

from web import core, views