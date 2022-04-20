from app.api.api_client import ApiClient


def test_login_succesfull():
    client = ApiClient()
    assert client.login() is not None
