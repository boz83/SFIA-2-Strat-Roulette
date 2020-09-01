#! /bin/bash
cd SFIA-2-Strat-Roulette
cd service-1
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest-cov
pip3 install flask_testing
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service-2
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service-3
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service-4
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..