#! /bin/bash
export TEST_SECRET_KEY=${TEST_SECRET_KEY} 
export TEST_DATABASE_URI=${TEST_DATABASE_URI} 

cd ./service1
pip3 install -r requirements.txt
python3 -m pytest --cov=application 
cd ..

cd ./service2
python3 -m pytest --cov=application
cd ..


cd ./service3
python3 -m pytest --cov=application
cd ..


cd ./service4
python3 -m pytest --cov=application
cd ..