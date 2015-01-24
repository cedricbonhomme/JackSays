#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from web import app, socketio

port = int(os.environ.get('PORT', 5000))
socketio.run(app, host='0.0.0.0', port=port)
