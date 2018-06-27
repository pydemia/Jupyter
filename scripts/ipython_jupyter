# Jupyter

## `Ipython` & `Jupyter`
### Installation

```sh
pip install ipython jupyter
conda install nb_conda
conda install -c conda-forge nb_conda_kernels
conda install ipykernel
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


## `Jupyter notebook`
### Installation

```sh
pip install jupyter
jupyter notebook
jupyter notebook --generate-config
```

### Extensions

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

#### Theme

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


## `Jupyter kernelgateway`
### Installation

## `JupyterHub`
### Installation

##`JupyterLab`]()
### Installation

## Utils
### Prepare a hashed password
### Launch as a `daemon`
