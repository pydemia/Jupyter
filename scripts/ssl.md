# SSL/TSA

```sh
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python-certbot-apache 
```

```sh
sudo certbot certonly -d <example.com>
```

```sh
sudo chown <user> /usr/local/etc/letsencrypt/live
sudo chown <user> /usr/local/etc/letsencrypt/archive
```

