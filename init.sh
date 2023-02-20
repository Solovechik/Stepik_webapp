#/usr/bin/sh

# sudo ln -sf $HOME/web/etc/nginx.conf /etc/nginx/sites-enabled/default
# sudo /etc/init.d/nginx restart
# source ~/web/ask/venv/bin/activate
# gunicorn -w 2 -b 0.0.0.0:8080 --chdir ~/web hello:hello & gunicorn -w 2 -b 0.0.0.0:8000 --chdir ~/web/ask ask.wsgi
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database stepik_webapp"
sudo mysql -uroot -e "create user 'box'@'localhost' identified by 'mydjangopassword'"
sudo mysql -uroot -e "grant all on stepik_webapp.* to 'box'@'localhost'"
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate
