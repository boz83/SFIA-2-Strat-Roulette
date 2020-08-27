from flask import render_template, redirect, url_for, request, jsonify
import requests
from application import app


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')


@app.route('/generate_strat', methods=['GET', 'POST'])
def generate_strat():
  map = requests.get('http://service2:5001/get_map')
  strat = requests.get('http://service3:5002/get_strat')
  return render_template('strat.html', map_name = map.text, strategy=strat.text, title='Strategy')