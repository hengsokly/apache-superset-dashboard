# Apache-superset-dashboard
is an experiment project for using apache-superset dashboard visualization data

## Development Setup

### Prerequisit and Installation
- Install [Docker](https://docs.docker.com/get-docker/)
- install [Docker Compose](https://docs.docker.com/compose/install/)

### Docker development
Use the ```docker-compose.yml``` file to build a development environment mounting the current folder and running the application in a development environment.

Run the following commands to start the application.
```
$ docker-compose up
```
And visit [localhost:8088](http://localhost:8088)

## Seed data
### Create an account
```
docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin
```

### Configure Superset
```
$ docker exec -it superset superset db upgrade &&
  docker exec -it superset superset load_examples &&
  docker exec -it superset superset init
```

## Login with a custom oAuth2 provider application
1) Assume that we have a Ruby on Rails application setup oAuth2 provider with the [doorkeeper](https://github.com/doorkeeper-gem/doorkeeper) gem
- Start the application with port [localhost:3000](http://localhost:3000)
- Go to the link http://localhost:3000/oauth/applications and create a new application
- The callback URL: ```http://localhost:8088/oauth-authorized/generic_oauth```
- Then copy the ```client_id``` and ```client_secret``` for the following uses.

2) open ```./app/superset_config.py``` and update
```
from flask_appbuilder.security.manager import AUTH_OAUTH

# Set the authentication type to OAuth
AUTH_TYPE = AUTH_OAUTH
CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

OAUTH_PROVIDERS = [
    {   'name':'generic_oauth',
        'token_key':'access_token', # Name of the token in the response of access_token_url
        'icon':'fa-address-card',   # Icon for the provider
        'remote_app': {
            'client_id':'CLIENT_ID',  # Client Id (Identify Superset application)
            'client_secret':'CLIENT_SECRET', # Secret for this Client Id (Identify Superset application)
            'client_kwargs':{
                'scope': 'read'               # Scope for the Authorization
            },
            'api_base_url':'API_BASE_URL',
            'access_token_url':'ACCESS_TOKEN_URL',
            'authorize_url':'AUTHORIZE_URL'
        }
    }
]

# Will allow user self-registration, allowing to creation of Flask users from Authorized User
AUTH_USER_REGISTRATION = True

# The default user self-registration role
AUTH_USER_REGISTRATION_ROLE = "Public"
```

**Replace these variables**
```
- CLIENT_ID=client_id from the Rails app
- CLIENT_SECRET=client_secret from the Rails app
- API_BASE_URL=http://[ip_address]:3000/oauth/token/info
- ACCESS_TOKEN_URL=http://[ip_address]:3000/oauth/token
- AUTHORIZE_URL=http://[ip_address]:3000/oauth/authorize
```
