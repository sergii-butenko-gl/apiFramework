from app.api.base_request import BaseRequests
from app.api.urls import Urls
from config.config import Config


class ApiClient(BaseRequests):
    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r = self.get(Urls.LOGIN,
                     headers={'Authorization': 'Basic bWFpbGludGVzdEB1a3IubmV0Om1haWxpbnRlc3RAdWtyLm5ldA=='})
        self.token = r.json().get('token')
        return self.token

    def get_folders(self):
        r = self.get(Urls.FOLDERS)
        r.raise_for_status()
