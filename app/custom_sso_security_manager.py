import logging
from superset.security import SupersetSecurityManager

class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        logging.debug("Oauth2 provider: {0}.".format(provider))

        if provider == 'generic_oauth':
            # As example, this line request a GET to base_url + '/' + info with Bearer  Authentication,
            # and expects that authorization server checks the token, and response with user details
            me = self.appbuilder.sm.oauth_remotes[provider].get('info').json()

            logging.debug("=============user: {0}".format(me))
            # logging.debug("=============user_data: {0}".format(me.json().get("email")))
            # logging.debug("=============user_data: {0}".format(me.json()["email"]))
            return { 'name' : me['email'], 'email' : me['email'], 'id' : me['email'], 'username' : me['email'], 'first_name':'', 'last_name':''}
    ...
