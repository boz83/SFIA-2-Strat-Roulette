from flask import request, Response
import requests
from application import app
import random

@app.route('/get_rule', methods=['GET'])
def get_rule():
  rules = ['Gladiator: Only one person may leave spawn. When that person dies, the next person leaves.',
            'Russian Roulette: All players must press their autobuy key at the start of the round. Whatever the game buys for them, they have to use',
            'One mans trash: Every player buys his most hated gun and gives it to a teammate.',
            'Golden Gun: When the first person on your team gets a kill, everyone else must throw away their weapons and share the weapon that the first kill was made with (the golden gun)',
            ' One in the chamber: Buy 1 deagle, pass it to a teammate after 1 shot.',
            'Juan Deag: All 5 buy deagles - Go juan or go home!']
  rule = rules[random.randrange(6)]
  return Response(rule, mimetype='text/plain')