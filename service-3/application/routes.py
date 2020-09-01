from flask import request, Response
import requests
from application import app
import random


@app.route('/get_rule', methods=['GET', 'POST'])
def get_rule():
  map=request.data.decode('utf-8')
  if map=='Dust 2':
    rules=['Gladiator: Only one person may leave spawn. When that person dies, the next person leaves', 
           'One Mans Trash: Every player buys his most hated gun and gives it to a teammate']
    return Response(rules[random.randrange(0,2)],mimetype='text/plain')
  elif map=='Cobblestone':
    rules=['Golden Gun: When the first person on your team gets a kill, everyone else must throw away their weapons and share the weapon that the first kill was made with (the golden gun)',
           'One in the chamber: Buy 1 deagle, pass it to a teammate after 1 shot']
    return Response(rules[random.randrange(0,2)],mimetype='text/plain')
  elif map=='Inferno':
    rules=['Juan Deag: All 5 buy deagles - Go juan or go home!',
           'No Guns: Zeus and Knife Only']
    return Response(rules[random.randrange(0,2)],mimetype='text/plain')
  elif map=='Mirage':
    rules=['Juan Taps Only: You may only fire 1 shot at a time. You must drop or reload your weapon before shooting again',
           'Hurricane Katrina: When all of your teammates have been killed, they must continuously blow into their microphones as the remaining man tries to win the round']
    return Response(rules[random.randrange(0,2)],mimetype='text/plain')
  elif map=='Cache':
    rules= ['Clay Pigeon Shooting: Everyone buys a shotgun and must yell "PULL" whenever you fire at an enemy',
            'Battle of Waterloo: Everyone buys a scout and forms a firing squad. 3 at the back, 2 crouching in the front']
    return Response(rules[random.randrange(0,2)],mimetype='text/plain')
  else:
    return 'This is not a map in the active duty pool'