#/usr/bin/sh

sudo ln -sf $HOME/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
