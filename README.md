# Jupyter


## Conda 

```sh
conda install nb_conda
conda install -c conda-forge nb_conda_kernels
conda install ipykernel
```


## Jupyter Server

### Launch as a Daemon(Autostart)

Create a Service: 

```sh
sudo vi /etc/systemd/system/jupyter.service
```

```sh
[Unit]
Description=Jupyter Notebook

[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/bfortuner/anaconda3/bin/jupyter-notebook --config=/home/bfortuner/.jupyter/jupyter_notebook_config.py
User=bfortuner
Group=bfortuner
WorkingDirectory=/home/bfortuner/workplace
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Then,
```sh
systemctl enable jupyter.service
systemctl daemon-reload
systemctl restart jupyter.service
```


## Jupyter Kernels

### conda environment Python2.7

```sh
conda create -n Python2.7 python=2.7 ipykernel -y
source activate Python2.7
python -m ipykernel install --user

```

### R kernel

```sh
sudo echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | sudo tee -a /etc/apt/sources.list
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
gpg -a --export E084DAB9 | sudo apt-key add -
sudo apt-get update
sudo apt-get install r-base r-base-dev
sudo apt-get install libcurl4-openssl-dev libssl-dev

```

```r
install.packages('devtools')
install.packages('httr')
install.packages('openssl')
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()

# Sys.getenv('PATH') : If jupyter-kernelspec is not found in $PATH

```
