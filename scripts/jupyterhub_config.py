#  Users should be properly informed if this is enabled.
#c.JupyterHub.admin_access = False

## The base URL of the entire application
#c.JupyterHub.base_url = '/'

## The config file to load
#c.JupyterHub.config_file = 'jupyterhub_config.py'

## DEPRECATED: does nothing
#c.JupyterHub.confirm_no_ssl = False

#  Loaded from the JPY_COOKIE_SECRET env variable by default.
#c.JupyterHub.cookie_secret = b''

## File in which to store the cookie secret.
#c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

## The ip for this process
c.JupyterHub.hub_ip = '0.0.0.0'

## The port for this process
c.JupyterHub.hub_port = 8081

## The public facing ip of the whole application (the proxy)
c.JupyterHub.ip = ''

#c.JupyterHub.load_groups = {}

## Specify path to a logo image to override the Jupyter logo in the banner.
#c.JupyterHub.logo_file = ''

## The public facing port of the proxy
#c.JupyterHub.port = 8000
#c.JupyterHub.port = 443
## The ip for the proxy API handlers
#c.JupyterHub.proxy_api_ip = '127.0.0.1'

## The port for the proxy API handlers
#c.JupyterHub.proxy_api_port = 0


c.JupyterHub.ssl_cert = '/home/pydemia/.ssl/jupyterhub.crt'
c.JupyterHub.ssl_key = '/home/pydemia/.ssl/jupyterhub.key'

#  Defaults to an empty set, in which case no user has admin access.
#c.Authenticator.admin_users = set()

## Dictionary mapping authenticator usernames to JupyterHub users.
#  
#  Primarily used to normalize OAuth user names to local users.
#c.Authenticator.username_map = {}

## Regular expression pattern that all valid usernames must match.
#  
#  If a username does not match the pattern specified here, authentication will
#  not be attempted.
#  
#  If not set, allow any username.
#c.Authenticator.username_pattern = ''

c.Authenticator.whitelist = set(['pydemia', 'tensorflow', 'python'])
