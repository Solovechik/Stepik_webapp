#/usr/bin/sh

sudo ln -sf $HOME/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -w 2 -b 0.0.0.0:8080 --chdir ~/web hello:hello
