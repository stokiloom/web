sudo rm /etc/nginx/sites-available/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart
