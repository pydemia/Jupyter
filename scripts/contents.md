# Jupyter

---

* [`Ipython` & `Jupyter`](#ipython--jupyter)
  - [Install a kernel (with `conda env`)](#install-a-kernel-with-conda-env)
* [`Jupyter notebook`](#jupyter-notebook)
* [`Jupyter kernelgateway`](#jupyter-kernelgateway)
* [`JupyterHub`](#jupyterhub)
* [`JupyterLab`(Experimental)](#jupyterlabexperimental)
* [`Utils`](#utils)
  - [Prepare a hashed password](#prepare-a-hashed-password)
  - [Launch as a `daemon`](#launch-as-a-daemon)
  - [SSL for Encrypted Communication](#ssl-for-encrypted-communication)
  - [Customization](#customization)
    - [Extensions](#extensions)
    - [Themes](#themes)
    - [Variable Explorer](#variable-explorer)


---


## `Ipython` & `Jupyter`
### Installation

```sh
pip install ipython jupyter
conda install nb_conda jupyter_contrib_nbextensions ipykernel ipywidgets ipyparallel -y
conda install -c conda-forge nb_conda_kernels

pip install jupyter_tensorboard
pip install nbgrader

```

### Install a kernel (with `conda env`)
#### `python`

```sh
conda create -n tf-py36 python=3.6 ipykernel -y
source activate tf-py36
python -m ipykernel install --user --name tf-py36 --display-name "Tensorflow Python3.6 (conda env)"
```

#### `R`

```sh
sudo apt-get install gnupg gnupg1 gnupg2 -y
```


```sh
echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/" | tee -a /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
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

install.packages('git2r', type='mac.binary.mavericks')

# Sys.getenv('PATH') : If jupyter-kernelspec is not found in $PATH

```

In `Hydrogen`, install `language-r` for `R-kernel`.


#### `julia`

```sh
julia
```

```jl
Pkg.add("IJulia")
```

```sh
vim .local/share/jupyter/kernels/julia-0.6/kernel.json
```

#### `scala`
#### `matlab`
#### `octave`

### Manage a kernel
#### Show it

```sh
jupyter kernelspec list
```

#### Launch it(`activate.d`)

```sh
> source activate tf-py36
(tf-py36)> source deactivate
```

#### Remove it

```sh
jupyter kernelspec remove <kernel name>
```

### Connect to a kernel
#### Webbrowser
#### Websocket


## `Jupyter notebook`
### Installation

```sh
pip install jupyter
jupyter notebook

```

### Config

```sh
jupyter notebook --generate-config
vim ~/.jupyter/jupyter_notebook_config.py

```
[`jupyter_notebook_config.py`](jupyter_notebook_config.py)


## `nbgrader`

### Installation

```sh
pip install nbgrader
conda install jupyter
conda install -c conda-forge nbgrader -y

jupyter nbextension install --user --py nbgrader --overwrite
jupyter nbextension enable --user --py nbgrader
jupyter serverextension enable --user --py nbgrader

jupyter nbextension enable --user create_assignment/main
```



## `Jupyter kernelgateway`
### Installation

```py
pip install jupyter_kernel_gateway

```

### Config

```sh
jupyter kernelgateway --generate-config
vim ~/.jupyter/jupyter_kernel_gateway_config.py
```
[`jupyter_kernel_gateway_config.py`]()


## `JupyterHub`

**__ROOT USER ONLY__**

### Installation

```sh
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
apt-get install nodejs
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -

apt-get install -y nodejs
apt-get update

npm -v
npm install -g configurable-http-proxy
python3 -m pip install notebook
sudo easy_install virtualenv
easy_install "module"
```

For helps:
```sh
jupyterhub -h
configurable-http-proxy -h
```

```sh
python3 -m pip install jupyterhub

```

```sh
jupyterhub --ip 10.0.1.2 --port 443 --ssl-key my_ssl.key --ssl-cert my_ssl.cert
```

### Config

```sh
cd
jupyterhub --generate-config
mv jupyterhub_config.py .jupyter/
mkdir /usr/local/share/jupyter_conf.d
mv jupyterhub_config.py /usr/local/share/jupyter_conf.d/


```
[`jupyterhub_config.py`]()


### Kernel(with `conda`, not `virtualenv` in `/usr/bin/python3`)


```sh
cd /usr/local/bin
ln -s /usr/share/anaconda3/bin/conda ./conda
ln -s /usr/share/anaconda3/bin/activate ./activate
ln -s /usr/share/anaconda3/bin/deactivate ./deactivate
ln -s /usr/share/anaconda3/bin/jupyter ./jupyter
ln -s /usr/share/anaconda3/bin/ipykernel ./ipykernel
ln -s /usr/share/anaconda3/bin/deactivate ./deactivate

```

#### Install a kernel for all users (`--user` option disabled.)

```sh
conda create -n tf-py36 python=3.6 ipykernel -y
source activate tf-py36
python -m ipykernel install --name tf-py36 --display-name "Tensorflow Python3.6 (conda env)"
```

#### Remove a kernel

```sh
conda env remove --name tf-py36 -y
```



The following has been deprecated.
```sh
python3 -m pip install ipykernel

python3 -m ipykernel install --user --name [virtualEnv] --display-name "[displayKenrelName]"
python3 -m ipykernel install --user --name tf-py36 --display-name "Tensorflow (python3.6)" python=3.6
```

## `JupyterLab`(Experimental)

### Installation

```
conda install -c conda-forge jupyterlab

jupyter lab
```

### Config

```sh
jupyter lab --generate-config
```
[`jupyter_lab_config.py`]()


## `Utils`

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

### Launch as a `daemon`

```sh
cd /etc/systemd/system/
vim jupyter.service

```

```vi
[Unit]
Desciption=Jupyter Notebook

[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/pydemia/apps/anaconda3/bin/jupyter notebook
--config=/home/pydemia/.jupyter/jupyter_notebook_config.py
User=pydemia
Group=pydemia
WorkingDirectory=/home/pydemia/workspaces
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

```

```sh
systemctl daemon-reload
service jupyter start
```


### SSL for Encrypted Communication

```sh
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mycert.pem -out mycert.pem
```


### Customization

#### Extensions

[jupyter-contrib-nbextensions](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html)

Basic `nbextensions`:

```sh
conda install -c conda-forge jupyter_contrib_nbextensions -y
jupyter contrib nbextension install  # For all users.
jupyter contrib nbextension install --user

conda install -c conda-forge jupyter_nbextensions_configurator -y
jupyter nbextensions_configurator enable  # For all users
jupyter nbextensions_configurator enable --user

jupyter nbextension enable codefolding/main
```


`Tex` : An Extension for `pdf` support.

```sh
sudo apt-get install texlive-xetex -y
```

#### Themes

```sh
jupyter --data-dir  # /home/pydemia/.local/share/jupyter
```

```sh
cd ~/.local/share/jupyter
cd /usr/local/share/jupyter  # For root

mkdir -p nbextensions
cd nbextensions
mkdir jupyter_themes
cd jupyter_themes

wget https://raw.githubusercontent.com/merqurio/jupyter_themes/master/theme_selector.js

```

```sh
cd ..
jupyter nbextension enable jupyter_themes/theme_selector
```

#### Variable Explorer

```sh
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

```sh
jupyter nbextension enable varInspector/main
```
