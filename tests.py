# tests/test_tmdbwrapper.py

from Fed import *

def test_client():
    """Tests that the client is able to authorize"""

    response = Series(apikey = "127d428fd5917c2a35047e76f0b92fd0", 
                      series_id = 'GNPCA'
                )
    
    assert response.release()[0] == 200, 'more about the error'

test_client()