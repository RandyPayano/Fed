# tests/test_tmdbwrapper.py

from Series import *

def test_series():
    """Tests that the client is able to authorize"""

    response = Series(apikey = "127d428fd5917c2a35047e76f0b92fd0", 
                      series_id = 'GNPCA'
                )
    
    assert response.release()[0] == 200, 'more about the error'
    print("-- test_series-- : passed")


def test_sources_sources():
    pass