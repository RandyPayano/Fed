# tests/test_tmdbwrapper.py

from Fed import *

def test_client():
    """Tests that the client is able to authorize"""

    response = Series(apikey = "127d428fd5917c2a35047e76f0b92fd0", 
                      series_id = 'GNPCA'
                )
    print("===================")
    print(response.__dict__)
    #assert isinstance(response, dict)
    assert response is not None


test_client()