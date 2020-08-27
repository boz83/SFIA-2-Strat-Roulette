from flask import render_template, redirect, url_for, request, jsonify
import requests
from application import app


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')


@app.route('/generate_strat', methods=['GET', 'POST'])
def generate_strat():
  map = requests.get('http://34.105.142.187:5001/get_map')
  return render_template('strat.html', map_name = map.text)