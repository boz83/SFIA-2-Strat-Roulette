from flask import request,Response
import requests
from application import app
import random


@app.route('/get_map', methods=['GET'])
def get_map():
  maps = ['Dust 2', 'Cobblestone', 'Inferno', 'Mirage', 'Cache']
  map = maps[random.randrange(9)]
  return Response(map, mimetype='text/plain')
