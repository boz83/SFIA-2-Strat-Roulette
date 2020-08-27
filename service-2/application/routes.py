from flask import request, Response
import requests
from application import app
import random


@app.route('/get_strat', methods=['GET'])
def get_strat():
  strats = ['Bombsite A', 'Bombsite B', 'Mid Rush', 'Long Rush']
  strat = strats[random.randrange(4)]
  return Response(strat, mimetype='text/plain')
