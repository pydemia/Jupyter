# Jupyter


## Conda 

```sh
conda install nb_conda
conda install -c conda-forge nb_conda_kernels
conda install ipykernel
```

```sh
conda create -n Tensorflow python=3.5 ipykernel -y
source activate Tensorflow
python -m ipykernel install --user --name Tensorflow --display-name "Tensorflow Python3.5 (conda env)"

pip install --ignore-installed --upgrade \
 https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.0-cp35-cp35m-linux_x86_64.whl
 
```

Remove conda env:
```sh
conda env remove --name <Env Name>
```

## `activate.d` to set the environment variables for each env

```sh
cd anaconda3/envs/<your-envs>
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
```

edit `./etc/conda/activate.d/env_vars.s` first:

```sh
vim ./etc/conda/activate.d/env_vars.sh
```

```sh
#!/bin/sh

export MY_KEY='secret-key-value'
export MY_FILE=/path/to/my/file/

export OLD_LD_LIBRARY_PATH=${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=/your/path:${LD_LIBRARY_PATH}
```

then, edit `./etc/conda/deactivate.d/env_vars.sh` as follows:

```sh
vim ./etc/conda/deactivate.d/env_vars.sh
```

```sh
#!/bin/sh

unset MY_KEY
unset MY_FILE

export LD_LIBRARY_PATH=${OLD_LD_LIBRARY_PATH}
unset OLD_LD_LIBRARY_PATH
```


# Jupyter Extensions

```sh
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

conda install -c conda-forge jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user

jupyter nbextension enable codefolding/main
```

`Tex` : An Extension for `pdf` support.

```sh
sudo apt-get install texlive-xetex
```

for PDF:
```sh
pip install nbbrowserpdf
```

## Jupyter Kernel Gateway (`websocket` mode)

```py
pip install jupyter_kernel_gateway
jupyter kernelgateway --generate-config
vim ~/.jupyter/jupyter_kernel_gateway_config.py
```

# Jupyter Theme

## Installation

```sh
jupyter --data-dir  # /home/pydemia/.local/share/jupyter
```

```sh
cd ~/.local/share/jupyter
mkdir -p nbextensions
cd nbextensions
mkdir jupyter_themes
cd jupyter_themes

wget https://raw.githubusercontent.com/merqurio/jupyter_themes/master/theme_selector.js

```

## Activation

```sh
cd ..
jupyter nbextension enable jupyter_themes/theme_selector
```

Done.

# Variable Explorer

## Installation

```sh
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

## Activation
```sh
jupyter nbextension enable varInspector/main
```



## JupyterHub

```sh
sudo apt-get install npm nodejs-legacy
sudo npm install -g configurable-http-proxy
pip install jupyterhub
jupyterhub --generate-config

```


```sh
jupyterhub --ip 10.0.1.2 --port 443 --ssl-key my_ssl.key --ssl-cert my_ssl.cert
```

## JupyterLab

```
conda install -c conda-forge jupyterlab

jupyter lab
```

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

Remove:
```sh
conda env remove --name <Env Name>
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
devtools::install_github('IRkernel/IRkernel', force=TRUE)
IRkernel::installspec()

# Sys.getenv('PATH') : If jupyter-kernelspec is not found in $PATH

```

### Julia kernel

```sh
julia
```

```jl
Pkg.add("IJulia")
```

```sh
vim .local/share/jupyter/kernels/julia-0.6/kernel.json
```

### Show Kernels

```sh
jupyter kernelspec list
```

### Remove Kernels

```sh
jupyter kernelspec remove <kernel name>
```


# JupyterHub

## Installation

```sh
sudo apt-get install npm
python3 -m pip install jupyterhub
sudo npm install -g configurable-http-proxy
```

## Encryption

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout ___.key -out ___.crt
```

```sh
Generating a 1024 bit RSA private key
..................................++++++
..++++++
writing new private key to 'jupyterhub.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:KR
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:pydemia-server
Email Address []:
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

## Path to SSL certificate file for the public facing interface of the proxy
#
#  Use with ssl_key
c.JupyterHub.ssl_cert = '/home/pydemia/.ssl/___.crt'

## Path to SSL key file for the public facing interface of the proxy
#
#  Use with ssl_cert
c.JupyterHub.ssl_key = '/home/pydemia/.ssl/___.key'

```


# reST(`.rst`)

## Installation

```sh
sudo apt-get install pandoc
```
Done.


![varInspector_img](https://github.com/pydemia/Jupyter/blob/master/varInspector_image.png)
