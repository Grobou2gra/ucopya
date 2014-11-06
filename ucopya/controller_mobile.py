"""Interact with an Ucopia captive portal"""

import requests

class ControllerMobile(object):
    """The class reponsible for interacting with the captive portal"""

    __PORTAL_API = 'https://controller.mobile.lan/portal_api.php'

    def __init__(self, login, password):
        self.login    = login
        self.password = password
        self.session  = requests.Session()
        self.logged   = False

