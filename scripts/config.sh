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
curl https://get.docker.com | sudo bash
sudo usermod -aG docker $(whoami)
sudo apt update
sudo apt install -y curl jq
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
ansible-playbook -i inventory playbook.yaml