from flask import render_template, redirect, url_for, request, jsonify
import requests
from application import app


@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')


@app.route('/generate_strat', methods=['GET', 'POST'])
def generate_strat():
  map = requests.get('http://service-1:5001/get_map')
  strat = requests.get('http://service-2:5002/get_strat')
  rule = requests.get('http://service-3:5003/get_rule')
  return render_template('strat.html', map_name = map.text, strategy=strat.text, rule=rule.text, title='Strategy')