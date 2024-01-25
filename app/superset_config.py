# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# Alternatively you can set it with `SUPERSET_SECRET_KEY` environment variable.
# You MUST set this for production environments or the server will not refuse
# to start and you will see an error in the logs accordingly.
SECRET_KEY = 'your_secret_key_here'

# ----------------
from flask_appbuilder.security.manager import AUTH_DB, AUTH_OAUTH

# By default: Login with username and password
# AUTH_TYPE = AUTH_DB

# Uncomment below to enable login with OAuth2 - custom oauth provider
# from custom_sso_security_manager import CustomSsoSecurityManager
# # Set the authentication type to OAuth
# AUTH_TYPE = AUTH_OAUTH
# CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

# OAUTH_PROVIDERS = [
#     {   'name':'generic_oauth',
#         'token_key':'access_token', # Name of the token in the response of access_token_url
#         'icon':'fa-address-card',   # Icon for the provider
#         'remote_app': {
#             'client_id':'xZKnO3rhzC3-cDiYTnJbdPrT-mxeY-v-4QG-IwVBgKc',  # Client Id (Identify Superset application)
#             'client_secret':'PL57m8ja9MEJtHOhWtMjMQEYiNsi2dxTXvhocDqUsPw', # Secret for this Client Id (Identify Superset application)
#             'client_kwargs':{
#                 'scope': 'read'               # Scope for the Authorization
#             },
#             'api_base_url':'http://192.168.1.117:3000/oauth/token/info',
#             'access_token_url':'http://192.168.1.117:3000/oauth/token',
#             'authorize_url':'http://192.168.1.117:3000/oauth/authorize'
#         }
#     }
# ]

# # Will allow user self registration, allowing to create Flask users from Authorized User
# AUTH_USER_REGISTRATION = True

# # The default user self registration role
# AUTH_USER_REGISTRATION_ROLE = "Public"

# To enable create a user via API as it is in beta mode.
FAB_ADD_SECURITY_API = True
