#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, request
from flask.ext.socketio import SocketIO, emit, join_room, \
                                leave_room, close_room, disconnect

from web import socketio
from models import User, Game
from games import *

USERS = {}
NAMESPACE = "/test"
current_game=Game1()

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
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})

@socketio.on('my broadcast event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)

@socketio.on('join', namespace='/test')
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})

@socketio.on('leave', namespace='/test')
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(request.namespace.rooms),
          'count': session['receive_count']})

@socketio.on('close room', namespace='/test')
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])

@socketio.on('my room event', namespace='/test')
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])

@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    print(session)
    if 'user' in session:
        emit('my response',
         {'data': session['user'].nic+" has left", 'count': session['receive_count']},
         broadcast=True)
        del_user(session['user'])



def add_user(user):
    """
    Add a user.
    """
    if user.nic in USERS:
        return False
    else:
        USERS[user.nic]=user
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

