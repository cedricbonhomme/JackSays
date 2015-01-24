#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, request, g
from flask.ext.socketio import SocketIO, emit, join_room,  \
                                leave_room, close_room, disconnect

from flask.ext.login import LoginManager, login_user, logout_user, \
                            login_required, current_user, AnonymousUserMixin

from web import socketio
from models import User, Game
from games import *

USERS = {}
NAMESPACE = "/test"
current_game = None
from models import Game
from games.utils import WaitGame

from threading import Timer

def unload_game():
    global current_game
    print("finalized")
    current_game.finalize()

def load_game(game):
    global current_game
    print("loading "+game.game_id)
    current_game = game
    t = Timer(current_game.duration,unload_game)
    t.start()

@socketio.on('get game id', namespace='/test')
def get_current_game(msg):
    global current_game
    if current_game is None:
        w = WaitGame()
        w.duration = 60
        load_game(w)
    print("get game id ???")
    emit('game id',
         {'id': current_game.game_id,'param' : current_game.param})

@socketio.on('get game data', namespace='/test')
def get_game_data(msg):
    global current_game
    emit('game data',
         {'data': current_game.get_data(),'duration': current_game.duration})

@socketio.on('nic', namespace='/test')
def change_nic(message):
    usr = User(message['data'],0)
    if 'user' in session:
        del_user(session['user'])
    if add_user(usr):
        session['user']=usr

@socketio.on('game', namespace='/test')
def test_message(message):
    print session
    #current_game.user_input(session['user'],message['data'])

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response',
         {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    emit('my response',
         {'data': message['data']},
         broadcast=True)

@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms)})

@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms)})

@socketio.on('close room', namespace='/test')
def close(message):
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.'},
         room=message['room'])
    close_room(message['room'])

@socketio.on('my room event', namespace='/test')
def send_room_message(message):
    emit('my response',
         {'data': message['data']},
         room=message['room'])

@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    emit('my response',
         {'data': 'Disconnected!'})
    disconnect()

@socketio.on('connect', namespace='/test')
def test_connect():
    add_user(current_user)
    #print "current_user = "+current_user.nic
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    print(session)
    if 'user' in session:
        emit('my response',
         {'data': session['user'].nic+" has left", 'count': session['receive_count']},
         broadcast=True)
        #del_user(session['user'])



def add_user(user):
    """
    Add a user.
    """
    #if user.nic in USERS:
    #    return False
    #else:
        #USERS[user.nic]=user
    #print(nic)
    join_room(user.nic)
    emit('user list', {'data': ",".join([k for k in USERS])},broadcast=True)
    return True

def del_user(user):
    """
    Delete a user.
    """
    if user.nic not in USERS:
        return False
    else:
        close_room(user.nic)
        del USERS[user.nic]
        emit('user list', {'data': ",".join([k for k in USERS])},broadcast=True)
        return True

