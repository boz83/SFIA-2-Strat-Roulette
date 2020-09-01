#! /bin/bash
if ! [ -d SFIA-2-Strat-Roulette ]; then
    git clone https://github.com/boz83/SFIA-2-Strat-Roulette.git
fi
cd SFIA-2-Strat-Roulette
git pull
sudo apt install -y python3 python3-pip
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
docker-compose build
ansible-playbook -i inventory playbook.yaml