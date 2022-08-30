import requests 

class Fed:
    def __init__(self, key):
        self.apikey = key
        self.url_base = "https://api.stlouisfed.org/fred/"

    def get(self, URL, parameter = None):
        url_params = {}
        for key, value in parameter.items():
            if value is not None:
                url_params[key] = value
                
        response = requests.get(URL, params = url_params)
        return response.status_code, response.text    

    def _create_path(self, *args):
        """Create the URL path with the Fred endpoint and given arguments."""
        args = filter(None, args)
        path = self.url_base + '/'.join(args)
        return path


class series(Fed):
    def __init__(self, apikey):
        super().__init__(apikey)
        self.url_base = "https://api.stlouisfed.org/fred/series/"
    def categories():
        pass
    def observations():
        pass
    def release():
        pass

class Releases(Fed):
    pass

#https://api.stlouisfed.org/fred/series?series_id=GNPCA&api_key=127d428fd5917c2a35047e76f0b92fd0
a = series("127d428fd5917c2a35047e76f0b92fd0")
a._create_path("series", "nitida")


















"""
    Series
    fred/series - Get an economic data series.
    fred/series/categories - Get the categories for an economic data series.
    fred/series/observations - Get the observations or data values for an economic data series.
    fred/series/release - Get the release for an economic data series.
    fred/series/search - Get economic data series that match keywords.
    fred/series/search/tags - Get the tags for a series search.
    fred/series/search/related_tags - Get the related tags for a series search.
    fred/series/tags - Get the tags for an economic data series.
    fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
    fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
"""