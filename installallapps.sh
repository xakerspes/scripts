sudo apt-get update ;\
sudo apt-get install -y vim tmux htop git curl wget unzip zip gcc build-essential make less zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
git clone https://github.com/~/modbus_3.git
sudo apt install python3-venv -y
sudo apt install python3-pip -y
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate

