# Jupyter

---

* [`Ipython` & `Jupyter`](#ipython--jupyter)
  - [Install a kernel (with `conda env`)](#install-a-kernel-with-conda-env)
  - [Clone a kernel (with `conda env`)](#clone-it)
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

## `Anaconda`
### Installation

Anaconda archive: [link](https://repo.anaconda.com/archive)

```sh
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O install_anaconda3_py37.sh

sudo apt-get update -y
sudo apt-get install -y locales
sudo locale-gen --purge "en_US.UTF-8"

sudo bash -c "echo 'LC_ALL=en_US.UTF-8' >> /etc/environment"
sudo bash -c "echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen"
sudo bash -c "echo 'LANG=en_US.UTF-8' > /etc/locale.conf"

sudo apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

bash ./install_anaconda3_py37.sh \
  -b \
  -p $CONDA_PATH

sudo bash -c "echo 'export CONDA_PATH=\"/opt/anaconda3\"' >> /etc/profile"
sudo bash -c "echo 'export PATH=\"\$CONDA_PATH/bin:\$CONDA_PATH/sbin:\$CONDA_PATH/condabin:\$PATH\"' >> /etc/profile"

source /etc/profile
source /etc/bash.bashrc

sudo groupadd conda
sudo chgrp -R conda $CONDA_PATH
sudo chmod 770 -R $CONDA_PATH
sudo adduser $USER conda

conda init
source ~/.bashrc

```


## `Ipython` & `Jupyter`
### Installation

```sh
pip install ipython jupyter
conda install nb_conda ipykernel ipywidgets ipyparallel -y
conda install -c conda-forge nb_conda_kernels jupyter_contrib_nbextensions -y

pip install jupyter_tensorboard
pip install nbgrader

```

### Install a kernel (with `conda env`)
[Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

#### `python`

```diff
conda create -n tf-py36 python=3.6 ipykernel -y
-source activate tf-py36
+conda activate tf-py36
-python -m ipykernel install --user --name tf-py36 --display-name "Tensorflow Python3.6 (conda env)"
+python -m ipykernel install --user --name tf2-py37 --display-name "Py37-Tensorflow2 (conda env)"
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

```diff
-install.packages('devtools')
-install.packages('httr')
-install.packages('openssl')
-install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'))
-devtools::install_github('IRkernel/IRkernel', force=TRUE)
+install.packages('IRkernel')
IRkernel::installspec()

-install.packages('git2r', type='mac.binary.mavericks')

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

```vim
export SCALA_VERSION_FOR_ALMOND=2.12.8
export ALMOND_VERSION=0.5.0
```

```sh
cd git
https://github.com/almond-sh/almond
curl -Lo coursier https://git.io/coursier-cli
chmod +x coursier
./coursier bootstrap \
    -r jitpack \
    -i user -I user:sh.almond:scala-kernel-api_$SCALA_VERSION_FOR_ALMOND:$ALMOND_VERSION \
    sh.almond:scala-kernel_$SCALA_VERSION_FOR_ALMOND:$ALMOND_VERSION \
    -o almond

./almond --install
#Installed scala kernel under /home/pydemia/.local/share/jupyter/kernels/scala
```

#### `matlab`

```sh
pip install matlab_kernel
```

```vim
cat ~/.jupyter/matlab_kernel_config.py
c.MatlabKernel.plot_settings = dict(format='svg')
```

#### `octave`

```sh
pip install octave_kernel
```

#### `JavaScript`

```diff
-sudo apt-get install nodejs-legacy npm ipython ipython-notebook
+sudo apt-get install nodejs-legacy npm
-sudo npm install -g ijavascript
+npm install -g ijavascript
ijsinstall
```


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

#### Clone it

```sh
conda create --name tf2-py36 --clone tf-py36
```

or

```sh
conda env create -f environment.yml
```

#### Archive it

```sh
conda env export > environment.yml
```

#### Remove it

```sh
conda env remove -n ENV_NAME
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
vim pydemia-server-san.cnf

#[req]
#default_bits       = 2048
#distinguished_name = req_distinguished_name
#req_extensions     = v3_req
#x509_extensions    = v3_req
#
#[req_distinguished_name]
#commonName          = {{ common_name }} Common Name (e.g. server FQDN or YOUR name)
#emailAddress        = {{ ssl_certs_email }} Email Address
#organizationName    = {{ ssl_certs_organization }} Organization Name (eg, company)
#stateOrProvinceName = {{ ssl_certs_state }} State or Province Name (full name)
#localityName        = {{ ssl_certs_locality }} Locality Name (eg, city)
#countryName         = {{ ssl_certs_country }} Country Name (2 letter code)
#

#[ req_ext ]
#subjectAltName = @alt_names

#[v3_req]
## The extentions to add to a self-signed cert
#subjectKeyIdentifier = hash
#basicConstraints     = critical,CA:false
#subjectAltName       = DNS:{{ common_name }}
#keyUsage             = critical,digitalSignature,keyEncipherment
#--------------------------------------------------------------------

[req]
default_bits       = 2048
distinguished_name = req_distinguished_name
req_extensions     = req_ext
x509_extensions    = req_ext

[req_distinguished_name]
commonName          = {{ common_name }} Common Name (e.g. server FQDN or YOUR name)
emailAddress        = {{ ssl_certs_email }} Email Address
organizationName    = {{ ssl_certs_organization }} Organization Name (eg, company)
stateOrProvinceName = {{ ssl_certs_state }} State or Province Name (full name)
localityName        = {{ ssl_certs_locality }} Locality Name (eg, city)
countryName         = {{ ssl_certs_country }} Country Name (2 letter code)
commonName_default          = pydemia
emailAddress_default        = pydemia@gmail.com
organizationName_default    = pydemia-org
stateOrProvinceName_default = Gyeonggi-do
localityName_default        = Seongnam-si
countryName_default         = KR


[ req_ext ]
subjectAltName = @alt_names
#subjectAltName_default = DNS:ubuntu.pydemia.org

[ alt_names ]
DNS.1 = ubuntu.pydemia.org
DNS.2 = ubuntu.pydemia.com
```


```sh

openssl genrsa -rand rand.dat -des3 1024 > pydemia-CA.key # pass-phrase:pydemia
#openssl rsa -in ./pydemia-CA.key -out ./pydemia-CA-nocrpyt.key
openssl rsa -in ./pydemia-CA.key -out ./pydemia-CA.key
openssl req -new -key pydemia-CA.key > pydemia-CA.csr -config pydemia-server.cnf
openssl req -key pydemia-CA.key -x509 -nodes -sha1 -days 3650 -in pydemia-CA.csr -out pydemia-CA.crt -config pydemia-server.cnf


openssl md5 * > rand.dat
openssl genrsa -rand rand.dat -des3 1024 > pydemia-CAkey.pem #pass-phrase:pydemia
openssl req -new -key pydemia-CAkey.pem > pydemia-CAcsr.pem
openssl req -key pydemia-CAkey.pem -x509 -nodes -sha1 -days 3650 -in pydemia-CAcsr.pem -out pydemia-CAcrt.pem
openssl rsa -in ./pydemia-CA.key -out ./pydemia-CA-nocrpyt.key

```


```sh
vim ~/.ssl/pydemia_server_CA_config.cnf

default_bits        = 2048
distinguished_name  = dn
x509_extensions     = san
req_extensions      = san
extensions          = san
prompt              = no
[ dn ]
countryName         = KR
stateOrProvinceName = Gyeonggi-do
localityName        = Seongnam-si
organizationName    = pydemia-org
[ san ]
subjectAltName      = DNS:ubuntu.pydemia.com
```

```sh
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn

[dn]
C=DE
ST=Gyeonggi-do
L=Seongnam-si
O=head
OU=pydemia_server_RootCA
emailAddress=pydemia@gmail.com
CN = server.pydemia

```

```sh
openssl genrsa -out pydemia_server_rootCA.key 2048
openssl req -x509 -new -nodes -key pydemia_server_rootCA.key -sha256 -days 3650 -out pydemia_server_rootCA.pem
openssl req -x509 -sha256 -days 365 -key pydemia_server_rootCA.key -out pydemia_server_rootCA.crt -config pydemia_server_CA_config.cnf


Here is a solution that works for me:

#Create CA key and cert

openssl genrsa -out pydemia_server_rootCA.key 2048
openssl req -x509 -new -nodes -key pydemia_server_rootCA.key -sha256 -days 3650 -out pydemia_server_rootCA.pem

#Create server_rootCA.csr.cnf

pydemia_server_rootCA.csr.cnf
#[req]
#default_bits = 2048
#prompt = no
#default_md = sha256
#distinguished_name = dn
#
#[dn]
#C=DE
#ST=Berlin
#L=NeuKoelln
#O=Weisestrasse
#OU=local_RootCA
#emailAddress=ikke@server.berlin
#CN = server.berlin


#Create v3.ext configuration file
v3.ext
#authorityKeyIdentifier=keyid,issuer
#basicConstraints=CA:FALSE
#keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
#subjectAltName = @alt_names

[alt_names]
DNS.1 = server.berlin
Create server key

# openssl req -new -sha256 -nodes -out server.csr -newkey rsa:2048 -keyout server.key -config <( cat server_rootCA.csr.cnf )
Create server cert

# openssl x509 -req -in server.csr -CA server_rootCA.pem -CAkey server_rootCA.key -CAcreateserial -out server.crt -days 3650 -sha256 -extfile v3.ext
Add cert and key to Apache2 site-file, HTTPS (port 443) section

SSLCertificateFile    /etc/apache2/ssl/server.crt
SSLCertificateKeyFile    /etc/apache2/ssl/server.key
Copy server_rootCA.pem from the server to your machine..

# scp you@server.berlin:~/server_rootCA.pem .
.. and add it to Chromium browser

Chromium -> Setting -> (Advanced) Manage Certificates -> Import -> 'server_rootCA.pem'

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
cd "$(jupyter --data-dir)"
cd /usr/local/share/jupyter  # For root

mkdir -p nbextensions
cd nbextensions
mkdir jupyter_themes
cd jupyter_themes

wget https://raw.githubusercontent.com/merqurio/jupyter_themes/master/theme_selector.js

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
