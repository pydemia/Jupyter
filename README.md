# Jupyter


## Conda 

```sh
conda install nb_conda
conda install -c conda-forge nb_conda_kernels
conda install ipykernel
```

Remove conda env:
```sh
conda env remove --name <Env Name>
```


## Jupyter Server

### Prepare a hashed password

Automatically:
```sh
jupyter notebook password
Enter password:  ****
Verify password: ****
[NotebookPasswordApp] Wrote hashed password to /Users/you/.jupyter/jupyter_notebook_config.json
```

Manually:
```py
from notebook.auth import passwd
passwd()
Enter password:
Verify password:
#Out[2]: '<hashed_password>'
```

Then, `jupyter_notebook_config.py`:
```vi
c.NotebookApp.password = u'<hashed_password>'
```


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
ExecStart=/home/bfortuner/anaconda3/bin/jupyter-notebook 
#--config=/home/pydemia/.jupyter/jupyter_notebook_config.py
User=pydemia
Group=pydemia
WorkingDirectory=/home/pydemia/workplaces
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
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
/path/to/kernel/env/bin/python -m ipykernel install --prefix=/path/to/jupyter/env --name 'python-my-env'

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


### Show Kernels

```sh
jupyter kernelspec list
```

### Remove Kernels

```sh
jupyter kernelspec <kernel name>
```


# JupyterHub

## Installation

```sh
sudo apt-get install npm
python3 -m pip install jupyterhub
sudo npm install -g configurable-http-proxy
```

## Configuration

```sh
c.JupyterHub.base_url = '/'
c.JupyterHub.cleanup_proxy = True

## The ip for this process
c.JupyterHub.hub_ip = '127.0.0.1'

## The port for this process
c.JupyterHub.hub_port = 8081

## The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = ''

## The public facing port of the proxy
c.JupyterHub.port = 8000

## The ip for the proxy API hadlers
c.JupyterHub.proxy_api_ip = '127.0.0.1'

## The port for the proxy API hadlers
c.JupyterHub.peroxy_api_port = 0

## The IP address (or hostname) the single-user server should listen on.
c.Spawner.ip = '127.0.0.1'

## Maximum number of bytes a single-user notebook server is allowed to use.



```





