# Deploying Flask App with WSGI and Apache Server on Ubuntu 20.04 

sudo apt update
sudo apt upgrade

python3 --version //Python 3.8.10

sudo apt install apache2
sudo apt install libapache2-mod-wsgi-py3

sudo apt install python3-pip
sudo apt install python3-venv

sudo chown $USER /var/www
mkdir /var/www/flask
cd /var/www/flask
git clone https://github.com/EvgenyDavydenko/flask-venv-mod-wsgi
cd flask-venv-mod-wsgi

sudo bash -c "echo '127.0.0.1 flask.loc' >> /etc/hosts"
sudo cp flask.conf /etc/apache2/sites-available
sudo a2ensite flask.conf
sudo systemctl reload apache2

python3 -m venv venv
source venv/bin/activate

pip install flask