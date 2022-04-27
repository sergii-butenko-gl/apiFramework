from app.api.base_request import BaseRequests
from app.api.urls import Urls
from config.config import Config


class ApiClient(BaseRequests):

    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r = self.get(Urls.LOGIN,
                     headers={'Authorization': f'Basic {Config.LOGIN_TOKEN}'})
        self.token = r.json().get('token')
        return self.token

    def get_root_folder(self, token):
        """Method to get root folder"""
        r = self.get(Urls.ROOT_FOLDER,
                     headers={'x-token': token})
        return r.status_code

    def get_specific_folder(self, token):
        """Method to get specific folder"""
        r = self.get(Urls.SPECIFIC_FOLDER,
                     headers={'x-token': token})
        return r.status_code

    def get_count(self, token):
        """Method to get count folder"""
        r = self.get(Urls.FILES_COUNT_URL,
                     headers={'x-token': token})
        return r.json()

    def get_runs(self, token):
        """Method to get runs requests"""
        r = self.get(Urls.FILES_RESULT_URL_GET_RUN,
                     headers={'x-token': token})
        return r.status_code

    def get_analyses(self, token):
        """Method to get analyses requests"""
        r = self.get(Urls.FILES_RESULT_URL_GET_ANALYSES,
                     headers={'x-token': token})
        return r.status_code

    def get_artifacts(self, token):
        """Method to get artifacts requests"""
        r = self.get(Urls.FILES_RESULT_URL_GET_ARTIFACTS,
                     headers={'x-token': token})
        return r.status_code
