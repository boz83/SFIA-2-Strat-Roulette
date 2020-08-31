#! /bin/bash
ssh manager << EOF
scp /home/smtbore/SFIA-2-Strat-Roulette/docker-compose.yaml /home/jenkins/
export SECRET_KEY=${SECRET_KEY} 
export DATABASE_URI=${DATABASE_URI} 
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF