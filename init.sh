#/usr/bin/sh

sudo ln -s /home/$USER/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
