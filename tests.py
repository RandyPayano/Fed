# tests/test_tmdbwrapper.py

from Fed import TV

def test_client():
    """Tests that the client is able to authorize"""

    client = Feds()
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
