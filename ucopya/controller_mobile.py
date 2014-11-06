"""Interact with an Ucopia captive portal"""

import requests
import time

class ControllerMobile(object):
    """The class reponsible for interacting with the captive portal"""

    __PORTAL_API = 'https://controller.mobile.lan/portal_api.php'

    def __init__(self, login, password):
        self.login    = login
        self.password = password
        self.session  = requests.Session()
        self.logged   = False

    def do_login(self):
        """Log the user to the captive portal"""

        credentials = {
            'action'        : 'authenticate',
            'login'         : self.login,
            'password'      : self.password,
            'policy_accept' : 'false'
        }

        req = self.session.post(self.__PORTAL_API, credentials).json()

        if not 'error' in req:
            self.logged = True
            self.digest = req['user']['passwordDigest']['value']
            self.ssid   = req['user']['incomingZone']['value']

    def do_update(self):
        """Send a heartbeat to the captive portal to keep the connection up"""

        if not self.logged:
            self.login()

        keepalive = {
            'action'          : 'refresh',
            'login'           : self.login,
            'password_digest' : self.digest,
            'time'            : int(time.time())
        }

        req = self.session.post(self.__PORTAL_API, keepalive)

