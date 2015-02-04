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

from web.models import Game
from game1 import Game1
from utils import WaitGame, Still, Roma, Shake, Scream, Click, TSM

game_list = [Still(), Roma(), Shake(), Scream(), Click()]
