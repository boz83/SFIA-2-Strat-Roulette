from flask import request, Response
import requests
from application import app
import random

def decide_rule(map):
  mapRules = {
    'Dust 2': ['Gladiator: Only one person may leave spawn. When that person dies, the next person leaves', 
               'One Mans Trash: Every player buys his most hated gun and gives it to a teammate'],
    'Cobblestone': ['Golden Gun: When the first person on your team gets a kill, everyone else must throw away their weapons and share the weapon that the first kill was made with (the golden gun)',
                     'One in the chamber: Buy 1 deagle, pass it to a teammate after 1 shot'],
    'Inferno': ['Juan Deag: All 5 buy deagles - Go juan or go home!',
                'No Guns: Zeus and Knife Only'],
    'Mirage': ['Juan Taps Only: You may only fire 1 shot at a time. You must drop or reload your weapon before shooting again',
               'Hurricane Katrina: When all of your teammates have been killed, they must continuously blow into their microphones as the remaining man tries to win the round'],
    'Cache': ['Clay Pigeon Shooting: Everyone buys a shotgun and must yell "PULL" whenever you fire at an enemy',
              'Battle of Waterloo: Everyone buys a scout and forms a firing squad. 3 at the back, 2 crouching in the front']
  }

  return random.choice(mapRules[map])

@app.route('/get_rule', methods=['GET'])
def get_rule():
  map=request.data.decode('utf-8')
  mapRule=decide_rule(map)
  return Response(mapRule, mimetype='text/plain')

