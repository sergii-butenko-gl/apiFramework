from config.config import Config
import requests


class BaseRequests:
    """Class for calling HTTP requests"""

    def form_url(self, url):
        """Method to concat base url and api path"""
        return Config.BASE_URL + url

    def get(self, path, params=None, headers=None):
        """Reimplementation of GET method"""
        url = self.form_url(path)
        print(url)
        # rest asured
        return requests.get(url, params=params, headers=headers)

    def post(self, path, params):
        """Reimplementation of POST method"""
        url = self.form_url(path)
        # rest asured
        return requests.post(url, params)
