from flask import render_template, url_for
from application import app, db
from application.models import Strategys
import requests

@app.route('/')
@app.route('/home')
def home(): 
  return render_template('home.html', title='Home')


@app.route('/generate_strat', methods=['GET', 'POST'])
def generate_strat():
  map = requests.get('http://service-1:5001/get_map')
  strat = requests.get('http://service-2:5002/get_strat')
  rule = requests.post('http://service-3:5003/get_rule', data=map)
  db_data = Strategys(map=map.text, strategy=strat.text, rule=rule.text)
  db.session.add(db_data)
  db.session.commit()
  return render_template('strat.html', map_name = map.text, strategy=strat.text, rule=rule.text, title='Strategy')


@app.route('/generated_strats')
def generated_strats():
  stratData=Strategys.query.all()
  return render_template('all_strategys.html',title='Past Strategys',strats=stratData)